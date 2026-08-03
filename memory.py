import sqlite3
import os


DATABASE = "saeed_memory.db"



# =========================
# اتصال به دیتابیس
# =========================

def connect():

    return sqlite3.connect(
        DATABASE
    )



# =========================
# ساخت جدول‌ها
# =========================

def init_database():

    db = connect()
    cursor = db.cursor()


    # اطلاعات پروفایل حسین

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS profile (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        key TEXT UNIQUE,

        value TEXT

    )
    """)



    # خاطرات مهم

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS memories (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        category TEXT,

        content TEXT

    )
    """)



    # تاریخچه گفتگو

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS conversations (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        role TEXT,

        content TEXT

    )
    """)



    db.commit()
    db.close()



# =========================
# ذخیره پروفایل
# =========================

def save_profile(
    key,
    value
):

    db = connect()

    cursor = db.cursor()


    cursor.execute(
        """
        INSERT OR REPLACE INTO profile
        (key,value)

        VALUES (?,?)
        """,

        (
            key,
            value
        )
    )


    db.commit()
    db.close()



# =========================
# گرفتن پروفایل
# =========================

def get_profile():

    db = connect()

    cursor = db.cursor()


    cursor.execute(
        """
        SELECT key,value
        FROM profile
        """
    )


    result = cursor.fetchall()


    db.close()


    return result



# =========================
# ذخیره خاطره
# =========================

def save_memory(
    category,
    content
):

    db = connect()

    cursor = db.cursor()


    cursor.execute(
        """
        INSERT INTO memories
        (category,content)

        VALUES (?,?)
        """,

        (
            category,
            content
        )
    )


    db.commit()

    db.close()



# =========================
# خواندن خاطرات
# =========================

def get_memories():

    db = connect()

    cursor = db.cursor()


    cursor.execute(
        """
        SELECT category,content
        FROM memories
        ORDER BY id DESC
        """
    )


    result = cursor.fetchall()


    db.close()


    return result



# =========================
# ذخیره گفتگو
# =========================

def save_message(
    role,
    content
):

    db = connect()

    cursor = db.cursor()


    cursor.execute(
        """
        INSERT INTO conversations
        (role,content)

        VALUES (?,?)
        """,

        (
            role,
            content
        )
    )


    db.commit()

    db.close()



# =========================
# دریافت گفتگوهای اخیر
# =========================

def get_recent_messages(
    limit=30
):

    db = connect()

    cursor = db.cursor()


    cursor.execute(
        """
        SELECT role,content
        FROM conversations

        ORDER BY id DESC

        LIMIT ?
        """,

        (
            limit,
        )
    )


    result = cursor.fetchall()


    db.close()


    # برعکس کردن برای ترتیب درست گفتگو

    return list(
        reversed(result)
    )
