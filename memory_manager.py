import sqlite3
import os
from datetime import datetime


DB_NAME = "saeed_memory.db"


def init_memory_manager():
    """
    Initialize memory database
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT,
            category TEXT,
            created_at TEXT
        )
        """)

        conn.commit()
        conn.close()

        print("Memory Manager initialized")
        return True

    except Exception as e:
        print("Memory init error:", e)
        return False



def add_memory(content, category="general"):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO memories
            (content, category, created_at)
            VALUES (?, ?, ?)
            """,
            (
                content,
                category,
                str(datetime.now())
            )
        )

        conn.commit()
        conn.close()

        return True

    except Exception as e:
        print("Add memory error:", e)
        return False



def get_memories(limit=10):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT content, category
            FROM memories
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,)
        )

        data = cursor.fetchall()

        conn.close()

        return data

    except Exception as e:
        print("Read memory error:", e)
        return []



def search_memory(keyword):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT content, category
            FROM memories
            WHERE content LIKE ?
            """,
            (f"%{keyword}%",)
        )

        result = cursor.fetchall()

        conn.close()

        return result

    except Exception as e:
        print("Search memory error:", e)
        return []
