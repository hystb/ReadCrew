from crewai import Task
from agents.readme_structurer import readme_structurer

structure_readme_task = Task(
    description="From a raw README, structure the content with key sections.",
    agent=readme_structurer,
    expected_output="A structured README template with key sections outlined."
)
