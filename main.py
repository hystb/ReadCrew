from crewai import Crew
from agents import (
    readme_content_writer, readme_stylist, github_fetcher,
    readme_structurer, latex_formatter, final_reviewer
)
from tasks import (
    generate_readme_content_task,
    style_readme_task, fetch_github_data_task,
    structure_readme_task, format_latex_task, review_final_task
)

crew = Crew(
    agents=[
        readme_content_writer,
        readme_stylist,
        github_fetcher,
        readme_structurer,
        latex_formatter,
        final_reviewer
    ],
    tasks=[
        fetch_github_data_task,
        generate_readme_content_task,
        structure_readme_task,
        format_latex_task,
        style_readme_task,
        review_final_task
    ]
)

results = crew.kickoff()
print(results)
