from crewai import Agent

final_reviewer = Agent(
    name="Final Reviewer",
    role="Performs a final review of the README \
        before submission.",
    backstory="An AI quality assurance expert ensuring that all \
        deliverables meet high standards.",
    goal="Guarantee the final quality and coherence of the generated content.",
)
