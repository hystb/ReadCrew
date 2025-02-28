from crewai import Task
from agents.readme_stylist import readme_stylist

style_readme_task = Task(
    description="Enhance the README formatting with styles, badges, and \
        visual elements.",
    agent=readme_stylist,
    expected_output="A visually improved README file with enhanced formatting."
)
