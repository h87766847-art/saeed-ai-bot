import sqlite3


DATABASE = "saeed_memory.db"



def connect():

    return sqlite3.connect(
        DATABASE
    )



def init_goals():

    db = connect()

    cursor = db.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS goals (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        title TEXT,

        status TEXT,

        progress INTEGER

    )
    """)


    db.commit()

    db.close()



def add_goal(title):

    db = connect()

    cursor = db.cursor()


    cursor.execute(
        """
        INSERT INTO goals
        (title,status,progress)

        VALUES (?,?,?)
        """,

        (
            title,
            "شروع نشده",
            0
        )
    )


    db.commit()

    db.close()


    return "هدف ذخیره شد."



def get_goals():

    db = connect()

    cursor = db.cursor()


    cursor.execute(
        """
        SELECT title,status,progress
        FROM goals
        """
    )


    data = cursor.fetchall()


    db.close()


    return data



def update_progress(title, progress):

    db = connect()

    cursor = db.cursor()


    cursor.execute(
        """
        UPDATE goals

        SET progress=?

        WHERE title=?
        """,

        (
            progress,
            title
        )
    )


    db.commit()

    db.close()


    return "پیشرفت به‌روزرسانی شد."
