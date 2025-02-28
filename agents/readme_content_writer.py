from crewai import Agent
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool

wiki_query = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

wiki_tool = Tool(
    name="Wikipedia Search",
    func=lambda query: wiki_query.run(query),
    description="Searches Wikipedia for relevant information."
)

readme_content_writer = Agent(
    name="ReadMe Content Writer",
    role="Generates the raw content of the README, ensuring it covers \
        essential project details.",
    backstory="An AI specializing in technical documentation, ensuring \
        high-quality README generation.",
    goal="Provide a structured, informative, and complete README draft.",
    tools=[wiki_tool]
)
