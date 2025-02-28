from crewai import Task
from agents.final_reviewer import final_reviewer

review_final_task = Task(
    description="Perform a final review of the README \
        before submission.",
    agent=final_reviewer,
    expected_output="A validated and polished version of all generated files."
)
