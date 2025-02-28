from crewai import Task
from agents.latex_formatter import latex_formatter

format_latex_task = Task(
    description="Detect and format mathematical expressions in README \
        using LaTeX.",
    agent=latex_formatter,
    expected_output="A formatted README with properly \
        rendered LaTeX equations."
)
