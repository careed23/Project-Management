<div align="center">

# 🏗️ ☁️Strategic PMO Dashboard☁️ 🏗️

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=flat-square&logo=streamlit&logoColor=white)
![Repo Size](https://img.shields.io/github/repo-size/careed23/Project-Management?style=flat-square)

</div>

This repository contains a Streamlit-based Strategic Project Management Office (PMO) Dashboard. The dashboard is designed to provide a high-level overview of multiple projects, their statuses, budgets, and timelines, catering to business owners and stakeholders who need a quick, comprehensive understanding of their project portfolio.

## 🚀 Features

*   **Portfolio Overview**: High-level KPIs tracking total projects, status distribution, and total budget.
*   **Interactive Roadmap**: Gantt-style timeline for visualizing project schedules.
*   **Financial Analytics**: Pie charts and indicators for budget vs. actual spending, plus budget variance analysis.
*   **Data Persistence**: Integrated SQLite backend (`projects.db`) to manage and save project data locally.
*   **CRUD Operations**: Add, update, or delete projects directly through the "Manage Projects" tab in the dashboard interface.
*   **Interactive Filters**: A sidebar allows users to filter projects by status, providing dynamic views of the portfolio.

## 🛠️ Tech Stack

*   **Frontend**: [Streamlit](https://streamlit.io/)
*   **Visualizations**: [Plotly](https://plotly.com/python/)
*   **Database**: SQLite (via Python's `sqlite3` and `SQLAlchemy`)
*   **Language**: Python 3.8+

## 📦 Installation and Setup

### Prerequisites

*   Python 3.8 or higher
*   pip (Python package installer)

### Steps

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/careed23/Project-Management.git
    cd Project-Management
    ```

2.  **Create a Virtual Environment (Recommended):**
    *   **On Windows:**
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
    *   **On macOS/Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Application:**
    ```bash
    streamlit run app.py
    ```
    *Note: Upon the first run, the application will automatically create a local SQLite database file named `projects.db` in the root directory to store your project data.*

## 📖 Usage Instructions

The dashboard is divided into two main tabs:

1.  **📊 Portfolio Overview**: This is your read-only view. Use the sidebar filters to narrow down the projects by status. It displays KPIs, timelines, budget utilization, and progress metrics based on the data in your database.
2.  **⚙️ Manage Projects**: Use this tab to perform Data Entry. You can:
    *   **Add Project**: Enter details for a new project to add it to the database.
    *   **Update Project**: Select an existing project from the dropdown to modify its details (progress, budget spent, status, etc.).
    *   **Delete Project**: Permanently remove a project from the portfolio.

## 📂 Project Structure

*   `app.py`: Main entry point for the Streamlit application. Contains the tab layout and routing.
*   `requirements.txt`: Lists all required Python packages.
*   `src/`: Directory containing core application logic.
    *   `database.py`: Handles SQLite database initialization, loading data into Pandas DataFrames, and executing CRUD operations.
    *   `ui.py`: Contains reusable UI functions for rendering metrics, charts (Plotly), and custom styling.
*   `projects.db`: (Auto-generated) The local SQLite database file.

---

<div align="center">

## 💡 Best Practices for IT Project Management

</div>

### Introduction to IT Project Management

Embarking on your first tech project can feel daunting, but with a structured approach, it becomes manageable and rewarding. Unlike traditional projects, IT projects often involve rapidly evolving technologies, complex interdependencies, and a need for highly specialized skills. The key is to mitigate risks early, maintain clear communication, and remain flexible.

### 1. Define Your Vision and Goals (The "Why")

Before writing a single line of code, clearly articulate *why* you are undertaking this project.

*   **Business Objectives**: What specific business problems will this tech solution solve? (e.g., "Reduce customer support calls by 20%").
*   **Key Performance Indicators (KPIs)**: How will you measure success? Define quantifiable metrics that directly link to your business objectives.
*   **Scope**: What is definitively *in* scope, and what is *out*? Avoid "scope creep" by having a clear boundary from the start.

### 2. Choose the Right Methodology (Agile vs. Waterfall)

For your first tech project, an **Agile** approach is generally recommended.

*   **Agile (Scrum, Kanban)**: Best for projects with evolving requirements. It breaks work into small "sprints" (1-4 weeks), delivering working software frequently and allowing for continuous feedback.
*   **Waterfall**: Sequential phases (Requirements -> Design -> Implementation -> Testing). Less flexible, best only when requirements are 100% fixed and understood.

### 3. Build Your Team

*   **Key Roles**: You need a Project Manager (orchestrator), Product Owner (represents the business - often you!), Developers (builders), and QA Testers (quality check).
*   **Communication**: Lack of communication is the #1 reason projects fail. Hold daily stand-ups (15 mins) and regular reviews.

### 4. Risk Management (Don't Ignore the "What Ifs")

Proactively identify, assess, and mitigate potential risks (Technical, Resource, Budget, Scope). Define a mitigation strategy for each major risk before it happens.

### 5. Budget and Resource Management

Tech projects often run over budget. Add a contingency (15-25% of the total budget) for unforeseen issues. Use tools like this dashboard to track "Budget vs. Actual Spent."

### 6. Testing and Quality Assurance

Integrate testing throughout the development lifecycle, not just at the end. **User Acceptance Testing (UAT)** is critical: involve end-users to ensure the solution actually meets their needs before final launch.

### Key Takeaways:

*   **Start Small, Iterate Often**: Build a Minimum Viable Product (MVP) first.
*   **Your Involvement is Crucial**: You understand the business context best.
*   **Embrace Change**: Be prepared to adapt your vision as you learn more during development.
