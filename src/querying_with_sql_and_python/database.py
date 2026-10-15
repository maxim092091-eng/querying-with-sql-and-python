import sqlite3
from pathlib import Path

DATABASE_PATH = Path(__file__).resolve().parents[2] / "data" / "Chinook_Sqlite.sqlite"


def get_connection(db_path: str | Path = DATABASE_PATH) -> sqlite3.Connection:
    """Create and return a database connection"""
    return sqlite3.connect(db_path)
