from src.database import init_db, add_project, get_connection
from datetime import datetime

def seed_data():
    # Initialize DB
    init_db()
    
    # Check if data already exists
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM projects")
    count = cursor.fetchone()[0]
    conn.close()
    
    if count > 0:
        print("Database already seeded.")
        return

    # Sample Data
    projects = [
        ("Cloud Infrastructure Upgrade", "On Track", 75, "Alice Smith", 500000, 350000, datetime(2023, 1, 1), datetime(2023, 12, 31)),
        ("Customer Portal Redesign", "At Risk", 40, "Bob Johnson", 250000, 200000, datetime(2023, 3, 15), datetime(2023, 10, 30)),
        ("Security Audit 2023", "On Track", 90, "Charlie Davis", 100000, 85000, datetime(2023, 5, 1), datetime(2023, 7, 15)),
        ("Data Warehouse Migration", "Critical", 20, "Diana Prince", 750000, 600000, datetime(2023, 6, 1), datetime(2024, 3, 1)),
        ("Mobile App v2.0", "On Track", 55, "Edward Norton", 300000, 150000, datetime(2023, 2, 10), datetime(2023, 11, 15)),
        ("ERP Integration", "At Risk", 30, "Fiona Gallagher", 450000, 380000, datetime(2023, 4, 20), datetime(2024, 1, 15))
    ]

    for p in projects:
        add_project(*p)
    print("Database seeded successfully!")

if __name__ == "__main__":
    seed_data()
