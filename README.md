# 📚 ReadCrew

## 🔎 Project Overview
**ReadCrew** is an innovative README generator built using **CrewAi**. The application allows multiple agents to work collaboratively in generating and styling README files for various projects.

## 🛠️ Technologies Used
The project relies on the following Python packages, as listed in the `requirements.txt`:
- `crewai`
- `langchain`
- `langchain_community`
- `langchain-experimental`
- `langchain-openai`
- `openai`
- `requests`
- `nbformat`
- `matplotlib`
- `wikipedia`

## 📁 Important Files
### **`main.py`**
This is the main entry point of the application, which sets up Crew AI with various agents responsible for generating and styling README content. Below is a snippet of the `main.py` content:

```python
from crewai import Crew
from agents import (
    readme_content_writer,
    readme_stylist,
    github_fetcher,
    readme_structurer,
    latex_formatter,
    final_reviewer
)
from tasks import (
    generate_readme_content_task,
    style_readme_task,
    fetch_github_data_task,
    structure_readme_task,
    format_latex_task,
    review_final_task
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
```

### **`requirements.txt`**
This file specifies the dependencies required to run the project.

## 🚀 Usage
To get started with ReadCrew:
1. Clone the repository.
2. Install the dependencies from `requirements.txt`.
3. Execute the `main.py` script to initiate the README generation process.
