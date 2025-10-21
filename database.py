import sqlite3
from datetime import datetime

DB_NAME = "water_tracker.db"


def init_db():
    """Initialize database and create tables if not exists."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS water_intake(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT NOT NULL,
        intake_ml INTEGER NOT NULL,
        date TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


def log_intake(user_id: str, intake_ml: int):
    """Insert a water intake record into the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    date_today = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(
        "INSERT INTO water_intake (user_id, intake_ml, date) VALUES (?, ?, ?)",
        (user_id, intake_ml, date_today),
    )

    conn.commit()
    conn.close()


def get_intake_history(user_id: str):
    """Get all intake records for a given user."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT intake_ml, date 
        FROM water_intake 
        WHERE user_id = ?
        ORDER BY date DESC
    """, (user_id,))

    records = cursor.fetchall()
    conn.close()
    return records


