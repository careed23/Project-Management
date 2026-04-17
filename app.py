import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from src.database import load_projects, add_project, update_project, delete_project, init_db
from src.ui import (
    render_kpis, 
    render_timeline, 
    render_budget_pie, 
    render_progress_gauge, 
    render_budget_variance,
    color_status
)

# Initialize DB
init_db()

# Set page configuration
st.set_page_config(page_title="Strategic PMO Dashboard", layout="wide", page_icon="🚀")

# --- Custom Styling ---
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_stdio=True)

# --- Header ---
st.title("🚀 Strategic Project Management Dashboard")

# --- Load Data ---
df = load_projects()

# --- Sidebar Filters ---
st.sidebar.title("Dashboard Filters")
if not df.empty:
    status_filter = st.sidebar.multiselect("Filter by Status", options=df["Status"].unique(), default=df["Status"].unique())
    filtered_df = df[df["Status"].isin(status_filter)]
else:
    filtered_df = df

# --- Tabs ---
tab1, tab2 = st.tabs(["📊 Portfolio Overview", "⚙️ Manage Projects"])

with tab1:
    if df.empty:
        st.info("The portfolio is currently empty. Go to 'Manage Projects' to add your first project.")
    else:
        # --- KPI Section ---
        render_kpis(filtered_df)
        st.divider()

        # --- Main Layout ---
        left_col, right_col = st.columns([2, 1])

        with left_col:
            st.subheader("Project Portfolio Status")
            st.dataframe(
                filtered_df.style.map(color_status, subset=['Status']),
                use_container_width=True,
                hide_index=True
            )

            st.subheader("Project Timeline (Roadmap)")
            render_timeline(filtered_df)
            
            st.subheader("Budget Performance Analysis")
            render_budget_variance(filtered_df)

        with right_col:
            st.subheader("Budget Utilization (Spending Distribution)")
            render_budget_pie(filtered_df)

            st.subheader("Average Progress")
            render_progress_gauge(filtered_df)

        # --- Bottom Section: Risks & Issues ---
        st.divider()
        st.subheader("⚠️ Top Risks & Blocker Summary")
        risks_col1, risks_col2 = st.columns(2)

        with risks_col1:
            st.info("**Data Warehouse Migration:** Integration issues with legacy systems. Impact: High. Mitigation: Parallel run scheduled.")
        with risks_col2:
            st.warning("**ERP Integration:** Vendor delay on API delivery. Impact: Medium. Mitigation: Escalated to vendor account manager.")

with tab2:
    st.subheader("Manage Portfolio")
    
    action = st.radio("Action", ["Add Project", "Update Project", "Delete Project"], horizontal=True)
    
    if action == "Add Project":
        with st.form("add_form"):
            name = st.text_input("Project Name")
            col1, col2 = st.columns(2)
            with col1:
                status = st.selectbox("Status", ["On Track", "At Risk", "Critical"])
                owner = st.text_input("Owner")
                budget = st.number_input("Budget ($)", min_value=0.0)
            with col2:
                progress = st.slider("Progress %", 0, 100, 0)
                spent = st.number_input("Spent ($)", min_value=0.0)
            
            col3, col4 = st.columns(2)
            with col3:
                start_date = st.date_input("Start Date", datetime.now())
            with col4:
                end_date = st.date_input("End Date", datetime.now() + timedelta(days=90))
                
            submitted = st.form_submit_button("Add Project")
            if submitted:
                if name:
                    add_project(name, status, progress, owner, budget, spent, start_date, end_date)
                    st.success(f"Project '{name}' added successfully!")
                    st.rerun()
                else:
                    st.error("Project name is required.")

    elif action == "Update Project":
        if df.empty:
            st.warning("No projects to update.")
        else:
            project_to_update = st.selectbox("Select Project to Update", df["Project Name"].tolist())
            proj_data = df[df["Project Name"] == project_to_update].iloc[0]
            
            with st.form("update_form"):
                name = st.text_input("Project Name", value=proj_data["Project Name"])
                col1, col2 = st.columns(2)
                with col1:
                    status = st.selectbox("Status", ["On Track", "At Risk", "Critical"], 
                                         index=["On Track", "At Risk", "Critical"].index(proj_data["Status"]))
                    owner = st.text_input("Owner", value=proj_data["Owner"])
                    budget = st.number_input("Budget ($)", min_value=0.0, value=float(proj_data["Budget ($)"]))
                with col2:
                    progress = st.slider("Progress %", 0, 100, int(proj_data["Progress"]))
                    spent = st.number_input("Spent ($)", min_value=0.0, value=float(proj_data["Spent ($)"]))
                
                col3, col4 = st.columns(2)
                with col3:
                    start_date = st.date_input("Start Date", proj_data["Start Date"])
                with col4:
                    end_date = st.date_input("End Date", proj_data["End Date"])
                
                submitted = st.form_submit_button("Update Project")
                if submitted:
                    update_project(int(proj_data["id"]), name, status, progress, owner, budget, spent, start_date, end_date)
                    st.success(f"Project '{name}' updated successfully!")
                    st.rerun()

    elif action == "Delete Project":
        if df.empty:
            st.warning("No projects to delete.")
        else:
            project_to_delete = st.selectbox("Select Project to Delete", df["Project Name"].tolist())
            proj_data = df[df["Project Name"] == project_to_delete].iloc[0]
            
            if st.button("Confirm Delete"):
                delete_project(int(proj_data["id"]))
                st.success(f"Project '{project_to_delete}' deleted.")
                st.rerun()
