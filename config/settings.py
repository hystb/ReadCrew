from langchain_openai.llms import OpenAI
from langchain_community.llms import HuggingFacePipeline
from .llm_config import USE_LOCAL_LLM

if USE_LOCAL_LLM:
    llm = HuggingFacePipeline.from_pretrained("meta-llama/Llama-2-7b")
else:
    llm = OpenAI(
        model="gpt-4",
        temperature=0.5
    )
GITHUB_REPO_URL = input("Enter the GitHub repository URL: ").strip()
if not GITHUB_REPO_URL.startswith("https://github.com/"):
    raise ValueError("Invalid GitHub URL. Please enter a valid \
        GitHub repository link.")
if "/tree/" in GITHUB_REPO_URL:
    GITHUB_REPO_URL = GITHUB_REPO_URL.split("/tree/")[0]
GITHUB_REPO_URL = f"https://api.github.com/repos/{GITHUB_REPO_URL.replace('https://github.com/', '')}"
print(f"Fetching data from {GITHUB_REPO_URL}...")
