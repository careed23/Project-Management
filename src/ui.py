import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

def render_kpis(df):
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Projects", len(df))
    with col2:
        on_track = len(df[df["Status"] == "On Track"])
        pct = (on_track/len(df)*100) if len(df) > 0 else 0
        st.metric("On Track", on_track, delta=f"{pct:.1f}%")
    with col3:
        at_risk = len(df[df["Status"].isin(["At Risk", "Critical"])])
        st.metric("At Risk / Critical", at_risk, delta=f"-{at_risk}", delta_color="inverse")
    with col4:
        total_budget = df["Budget ($)"].sum()
        st.metric("Total Portfolio Budget", f"${total_budget:,.0f}")

def render_timeline(df):
    if df.empty:
        st.info("No projects to display.")
        return
        
    fig = px.timeline(
        df, 
        x_start="Start Date", 
        x_end="End Date", 
        y="Project Name", 
        color="Status",
        color_discrete_map={"On Track": "#28a745", "At Risk": "#ffc107", "Critical": "#dc3545"},
        hover_data=["Owner", "Progress"]
    )
    fig.update_yaxes(autorange="reversed")
    fig.update_layout(height=400, margin=dict(t=0, b=0, l=0, r=0))
    st.plotly_chart(fig, use_container_width=True)

def render_budget_pie(df):
    fig = px.pie(
        df, 
        values='Spent ($)', 
        names='Project Name', 
        hole=0.4,
        title="Spending Distribution"
    )
    st.plotly_chart(fig, use_container_width=True)

def render_progress_gauge(df):
    avg_progress = df["Progress"].mean() if not df.empty else 0
    fig = go.Figure(go.Indicator(
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
    fig.update_layout(height=300, margin=dict(t=50, b=0, l=30, r=30))
    st.plotly_chart(fig, use_container_width=True)

def render_budget_variance(df):
    if df.empty:
        return
    
    df['Variance'] = df['Budget ($)'] - df['Spent ($)']
    fig = px.bar(
        df,
        x='Project Name',
        y='Variance',
        title="Budget Variance (Remaining Budget)",
        color='Variance',
        color_continuous_scale='RdYlGn'
    )
    st.plotly_chart(fig, use_container_width=True)

def color_status(val):
    color = 'white'
    if val == 'On Track': color = '#d4edda'
    elif val == 'At Risk': color = '#fff3cd'
    elif val == 'Critical': color = '#f8d7da'
    return f'background-color: {color}; color: black'
