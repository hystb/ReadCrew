from crewai import Task
from agents.github_fetcher import github_fetcher
from config import GITHUB_REPO_URL

fetch_github_data_task = Task(
    description="Retrieve repository details from GitHub,\
        , including commits, issues, and technologies used, \
            or all important data to explain the porject.",
    agent=github_fetcher,
    expected_output="A text containing repository important data, all data \
        can be use to explain the project )."
)
