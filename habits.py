import sqlite3


DATABASE = "saeed_memory.db"



def connect():

    return sqlite3.connect(
        DATABASE
    )



def init_habits():

    db = connect()

    cursor = db.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS habits (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        title TEXT,

        done INTEGER DEFAULT 0,

        date TEXT

    )
    """)


    db.commit()

    db.close()



def add_habit(title):

    db = connect()

    cursor = db.cursor()


    cursor.execute(
        """
        INSERT INTO habits
        (title,done,date)

        VALUES (?,?,date('now'))

        """,

        (
            title,
            0
        )
    )


    db.commit()

    db.close()


    return "ماموریت روزانه ثبت شد."



def complete_habit(title):

    db = connect()

    cursor = db.cursor()


    cursor.execute(
        """
        UPDATE habits

        SET done=1

        WHERE title=?

        """,

        (
            title,
        )
    )


    db.commit()

    db.close()


    return "ماموریت انجام شد."



def show_habits():

    db = connect()

    cursor = db.cursor()


    cursor.execute(
        """
        SELECT title,done,date

        FROM habits

        ORDER BY id DESC

        """
    )


    result = cursor.fetchall()


    db.close()


    if not result:

        return "ماموریتی ثبت نشده."



    text = "ماموریت‌های حسین:\n"


    for title, done, date in result:

        status = "✅" if done else "⏳"

        text += (
            f"{status} {title} ({date})\n"
        )


    return text
