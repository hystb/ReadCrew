from crewai import Agent
from langchain_experimental.tools import PythonREPLTool
from langchain.tools import Tool

python_repl = PythonREPLTool()

latex_formatter_tool = Tool(
    name="LaTeX Code Executor",
    func=lambda x: python_repl.run(f"print(f'\\[{x}\\]')"),
    description="Executes Python code to format LaTeX expressions."
)

latex_formatter = Agent(
    name="LaTeX Formatter",
    role="Detects and reformats mathematical expressions in README and \
        Jupyter notebooks.",
    backstory="An AI expert in mathematical notation, ensuring that all \
        equations are correctly formatted using LaTeX.",
    goal="Ensure that all mathematical formulas are correctly \
        formatted using LaTeX.",
    tools=[latex_formatter_tool]
)
