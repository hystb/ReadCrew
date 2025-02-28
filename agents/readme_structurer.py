from crewai import Agent

readme_structurer = Agent(
    name="ReadMe Structurer",
    role="Analyzes the project files and proposes an optimal structure for \
        the README. no Contribution section, no License section.",
    backstory="An AI specializing in documentation architecture, ensuring \
        that README files follow industry best practices.",
    goal="Ensure the README includes all necessary sections and follows \
        best practices.",
)
