import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Set page configuration
st.set_page_config(page_title="Strategic PMO Dashboard", layout="wide")

# --- Mock Data Generation ---
def load_data():
    data = {
        "Project Name": [
            "Cloud Infrastructure Upgrade", 
            "Customer Portal Redesign", 
            "Security Audit 2023", 
            "Data Warehouse Migration", 
            "Mobile App v2.0",
            "ERP Integration"
        ],
        "Status": ["On Track", "At Risk", "On Track", "Critical", "On Track", "At Risk"],
        "Progress": [75, 40, 90, 20, 55, 30],
        "Owner": ["Alice Smith", "Bob Johnson", "Charlie Davis", "Diana Prince", "Edward Norton", "Fiona Gallagher"],
        "Budget ($)": [500000, 250000, 100000, 750000, 300000, 450000],
        "Spent ($)": [350000, 200000, 85000, 600000, 150000, 380000],
        "Start Date": [datetime(2023, 1, 1), datetime(2023, 3, 15), datetime(2023, 5, 1), datetime(2023, 6, 1), datetime(2023, 2, 10), datetime(2023, 4, 20)],
        "End Date": [datetime(2023, 12, 31), datetime(2023, 10, 30), datetime(2023, 7, 15), datetime(2024, 3, 1), datetime(2023, 11, 15), datetime(2024, 1, 15)]
    }
    df = pd.DataFrame(data)
    df['Remaining Budget'] = df['Budget ($)'] - df['Spent ($)']
    return df

df = load_data()

# --- Sidebar Filters ---
st.sidebar.title("Dashboard Filters")
status_filter = st.sidebar.multiselect("Filter by Status", options=df["Status"].unique(), default=df["Status"].unique())
filtered_df = df[df["Status"].isin(status_filter)]

# --- Header ---
st.title("🚀 Strategic Project Management Dashboard")
st.markdown("### High-Level Portfolio Overview")

# --- KPI Section ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Projects", len(filtered_df))
with col2:
    on_track = len(filtered_df[filtered_df["Status"] == "On Track"])
    st.metric("On Track", on_track, delta=f"{(on_track/len(filtered_df)*100):.1f}%" if len(filtered_df) > 0 else "0%")
with col3:
    at_risk = len(filtered_df[filtered_df["Status"].isin(["At Risk", "Critical"])])
    st.metric("At Risk / Critical", at_risk, delta=f"-{at_risk}", delta_color="inverse")
with col4:
    total_budget = filtered_df["Budget ($)"].sum()
    st.metric("Total Portfolio Budget", f"${total_budget:,.0f}")

st.divider()

# --- Main Layout ---
left_col, right_col = st.columns([2, 1])

with left_col:
    st.subheader("Project Portfolio Status")
    
    # Custom styling for the dataframe
    def color_status(val):
        color = 'white'
        if val == 'On Track': color = '#d4edda'
        elif val == 'At Risk': color = '#fff3cd'
        elif val == 'Critical': color = '#f8d7da'
        return f'background-color: {color}; color: black'

    st.dataframe(
        filtered_df.style.map(color_status, subset=['Status']),
        use_container_width=True,
        hide_index=True
    )

    st.subheader("Project Timeline (Roadmap)")
    fig_timeline = px.timeline(
        filtered_df, 
        x_start="Start Date", 
        x_end="End Date", 
        y="Project Name", 
        color="Status",
        color_discrete_map={"On Track": "#28a745", "At Risk": "#ffc107", "Critical": "#dc3545"},
        hover_data=["Owner", "Progress"]
    )
    fig_timeline.update_yaxes(autorange="reversed")
    fig_timeline.update_layout(height=400, margin=dict(t=0, b=0, l=0, r=0))
    st.plotly_chart(fig_timeline, use_container_width=True)

with right_col:
    st.subheader("Budget Utilization")
    fig_budget = px.pie(
        filtered_df, 
        values='Spent ($)', 
        names='Project Name', 
        hole=0.4,
        title="Spending Distribution"
    )
    st.plotly_chart(fig_budget, use_container_width=True)

    st.subheader("Average Progress")
    avg_progress = filtered_df["Progress"].mean()
    fig_gauge = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = avg_progress,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Portfolio Completion %"},
        gauge = {
            'axis': {'range': [0, 100]},
            'bar': {'color': "#31333F"},
            'steps' : [
                {'range': [0, 50], 'color': "#ffcccb"},
                {'range': [50, 80], 'color': "#fff3cd"},
                {'range': [80, 100], 'color': "#d4edda"}],
        }
    ))
    fig_gauge.update_layout(height=300, margin=dict(t=50, b=0, l=30, r=30))
    st.plotly_chart(fig_gauge, use_container_width=True)

# --- Bottom Section: Risks & Issues ---
st.divider()
st.subheader("⚠️ Top Risks & Blocker Summary")
risks_col1, risks_col2 = st.columns(2)

with risks_col1:
    st.info("**Data Warehouse Migration:** Integration issues with legacy systems. Impact: High. Mitigation: Parallel run scheduled.")
    st.warning("**ERP Integration:** Vendor delay on API delivery. Impact: Medium. Mitigation: Escalated to vendor account manager.")

with risks_col2:
    st.success("**Cloud Infrastructure:** Ahead of schedule. Resource reallocation possible for ERP project.")
    st.error("**Critical Blocker:** Security Audit found 2 major vulnerabilities in Customer Portal. Patching in progress.")
