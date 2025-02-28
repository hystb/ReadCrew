from crewai import Agent
from langchain.tools import Tool
from langchain_community.tools import RequestsGetTool
from langchain_community.utilities.requests import RequestsWrapper
from config import GITHUB_REPO_URL
import json
import base64


requests_wrapper = RequestsWrapper()
requests_tool = RequestsGetTool(requests_wrapper=requests_wrapper,
                                allow_dangerous_requests=True)


def fetch_github_files():
    """Fetch list of files from GitHub repository."""
    contents_url = GITHUB_REPO_URL + "/contents"
    response = requests_tool.run(contents_url)

    try:
        files = json.loads(response)
        file_list = [file["path"] for file in files if "path" in file]
        return {"files": file_list}
    except json.JSONDecodeError:
        return {"error": "Failed to fetch repository files"}


def fetch_github_file_contents():
    """Fetch content of each file in the repository and extract key
    information."""
    file_data = fetch_github_files()

    if "error" in file_data:
        return file_data

    extracted_contents = {}

    for file_path in file_data["files"]:
        file_url = f"{GITHUB_REPO_URL}/contents/{file_path}"
        file_response = requests_tool.run(file_url)

        try:
            file_info = json.loads(file_response)
            if "content" in file_info:
                content = base64.b64decode(file_info["content"]).decode("utf-8")
                extracted_contents[file_path] = content[:1000]
        except json.JSONDecodeError:
            extracted_contents[file_path] = "Error reading file content"

    return {"file_contents": extracted_contents}


file_fetch_tool = Tool(
    name="GitHub File Fetcher",
    func=fetch_github_files,
    description="Fetches the list of files from the GitHub repository."
)


file_content_tool = Tool(
    name="GitHub File Content Extractor",
    func=fetch_github_file_contents,
    description="Reads the content of each file and extracts important \
        information."
)


def fetch_github_metadata():
    """Fetch repository details from GitHub API and remove invalid keys."""
    response = requests_tool.run(GITHUB_REPO_URL)

    try:
        data = json.loads(response)
        clean_data = {k: v for k, v in data.items() if not k.startswith("_")}
        return clean_data
    except json.JSONDecodeError:
        return {"error": "Failed to parse GitHub API response"}


api_fetch_tool = Tool(
    name="GitHub API Fetcher",
    func=fetch_github_metadata,
    description="Fetches GitHub repository details such as commits, issues,\
        and metadata."
)

github_fetcher = Agent(
    name="GitHub Data Fetcher",
    role="Retrieves project details from GitHub, including commits, \
        issues, and technologies used.",
    backstory="An AI specialized in gathering GitHub project data for \
        analysis and documentation.",
    goal="Extract relevant information from GitHub to enhance README content.",
    tools=[api_fetch_tool, file_fetch_tool, file_content_tool]
)
