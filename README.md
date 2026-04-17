# Strategic PMO Dashboard

A high-level Project Management Office (PMO) dashboard built with Streamlit, Plotly, and SQLite. This tool provides executives and project managers with a real-time overview of portfolio health, budget utilization, and strategic roadmaps.

## 🚀 Features

- **Portfolio Overview**: High-level KPIs tracking total projects, status distribution, and total budget.
- **Interactive Roadmap**: Gantt-style timeline for visualizing project schedules.
- **Financial Analytics**: Pie charts and indicators for budget vs. actual spending.
- **Data Persistence**: Integrated SQLite backend to manage project data.
- **CRUD Operations**: Add, update, or delete projects directly through the dashboard interface.

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Visualizations**: [Plotly](https://plotly.com/python/)
- **Database**: SQLite
- **Language**: Python 3.9+

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/careed23/Project-Management.git
   cd Project-Management
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

## 📂 Project Structure

- `app.py`: Main entry point for the Streamlit application.
- `src/`: Core logic and UI components.
  - `database.py`: SQLite database management and CRUD logic.
  - `ui.py`: Reusable UI components and layout definitions.
- `data/`: Local storage for the SQLite database.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
