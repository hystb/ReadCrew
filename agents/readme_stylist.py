from crewai import Agent
from langchain_community.tools import FileSearchTool
from langchain.tools import Tool

file_search = FileSearchTool()

formatting_tool = Tool(
    name="Markdown Section Finder",
    func=lambda x: file_search.run({"file": x, "query": "## "}),
    description="Finds all sections in a Markdown README file for \
        improved styling."
)

readme_stylist = Agent(
    name="ReadMe Stylist",
    role="Enhances the README by adding formatting, styling, and elements \
        that improve readability.",
    backstory="An expert in technical writing, ensuring that documentation \
        is visually appealing.",
    goal="Make the README visually appealing and easy to navigate.",
    tools=[formatting_tool],
)
