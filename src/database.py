import sqlite3
import pandas as pd
from datetime import datetime
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

DB_PATH = "data/projects.db"

def init_db():
    """Initialize the database and create the projects table if it doesn't exist."""
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            status TEXT NOT NULL,
            progress INTEGER DEFAULT 0,
            owner TEXT,
            budget REAL,
            spent REAL,
            start_date TEXT,
            end_date TEXT
        )
    ''')
    conn.commit()
    conn.close()

def get_connection():
    return sqlite3.connect(DB_PATH)

def load_projects():
    """Load all projects from the database into a pandas DataFrame."""
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM projects", conn)
    conn.close()
    
    # Convert date strings back to datetime objects
    if not df.empty:
        df['start_date'] = pd.to_datetime(df['start_date'])
        df['end_date'] = pd.to_datetime(df['end_date'])
        df['Remaining Budget'] = df['budget'] - df['spent']
        # Rename columns to match existing UI expectations if necessary
        df = df.rename(columns={
            "name": "Project Name",
            "status": "Status",
            "progress": "Progress",
            "owner": "Owner",
            "budget": "Budget ($)",
            "spent": "Spent ($)",
            "start_date": "Start Date",
            "end_date": "End Date"
        })
    return df

def add_project(name, status, progress, owner, budget, spent, start_date, end_date):
    """Add a new project to the database."""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO projects (name, status, progress, owner, budget, spent, start_date, end_date)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (name, status, progress, owner, budget, spent, start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')))
        conn.commit()
        logger.info(f"Added project: {name}")
    except sqlite3.Error as e:
        logger.error(f"Error adding project: {e}")
        raise
    finally:
        conn.close()

def update_project(project_id, name, status, progress, owner, budget, spent, start_date, end_date):
    """Update an existing project."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE projects 
        SET name=?, status=?, progress=?, owner=?, budget=?, spent=?, start_date=?, end_date=?
        WHERE id=?
    ''', (name, status, progress, owner, budget, spent, start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'), project_id))
    conn.commit()
    conn.close()

def delete_project(project_id):
    """Delete a project."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM projects WHERE id=?', (project_id,))
    conn.commit()
    conn.close()
