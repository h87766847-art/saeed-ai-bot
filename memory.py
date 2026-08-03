import sqlite3
import os


DATABASE = "saeed_memory.db"


def connect():
    return sqlite3.connect(DATABASE)



def init_database():

    db = connect()
    cursor = db.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS profile (
        key TEXT PRIMARY KEY,
        value TEXT
    )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS memories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT,
        content TEXT
    )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS conversations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        role TEXT,
        content TEXT
    )
    """)


    db.commit()
    db.close()



def save_profile(key, value):

    db = connect()
    cursor = db.cursor()

    cursor.execute("""
    INSERT OR REPLACE INTO profile
    VALUES (?,?)
    """,
    (key,value))


    db.commit()
    db.close()



def get_profile():

    db = connect()
    cursor = db.cursor()


    cursor.execute(
        "SELECT * FROM profile"
    )


    data = cursor.fetchall()

    db.close()

    return data



def save_memory(category, content):

    db = connect()
    cursor = db.cursor()


    cursor.execute("""
    INSERT INTO memories
    (category,content)
    VALUES (?,?)
    """,
    (category,content))


    db.commit()
    db.close()



def get_memories():

    db = connect()
    cursor = db.cursor()


    cursor.execute(
        "SELECT category,content FROM memories"
    )


    data = cursor.fetchall()

    db.close()

    return data



def save_message(role, content):

    db = connect()
    cursor = db.cursor()


    cursor.execute("""
    INSERT INTO conversations
    (role,content)
    VALUES (?,?)
    """,
    (role,content))


    db.commit()
    db.close()



def get_recent_messages(limit=20):

    db = connect()
    cursor = db.cursor()


    cursor.execute("""
    SELECT role,content
    FROM conversations
    ORDER BY id DESC
    LIMIT ?
    """,
    (limit,))


    data = cursor.fetchall()

    db.close()


    return list(reversed(data))
