import pytest
import os
import pandas as pd
from datetime import datetime
from src.database import init_db, add_project, load_projects, DB_PATH

@pytest.fixture
def test_db():
    # Setup: Use a temporary test database
    original_db = DB_PATH
    test_db_path = "data/test_projects.db"
    import src.database
    src.database.DB_PATH = test_db_path
    init_db()
    yield
    # Teardown: Remove test database
    if os.path.exists(test_db_path):
        os.remove(test_db_path)
    src.database.DB_PATH = original_db

def test_init_db(test_db):
    assert os.path.exists("data/test_projects.db")

def test_add_and_load_project(test_db):
    add_project(
        "Test Project", "On Track", 50, "Tester", 1000.0, 500.0, 
        datetime(2023, 1, 1), datetime(2023, 6, 1)
    )
    df = load_projects()
    assert len(df) == 1
    assert df.iloc[0]["Project Name"] == "Test Project"
    assert df.iloc[0]["Status"] == "On Track"
    assert df.iloc[0]["Budget ($)"] == 1000.0
