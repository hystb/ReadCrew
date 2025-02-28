from crewai import Task
from agents.readme_content_writer import readme_content_writer

generate_readme_content_task = Task(
    description="Generate the raw content of the README based on \
        project informations",
    agent=readme_content_writer,
    expected_output="A structured README draft including project details, \
        or all important data to explain the project."
)
