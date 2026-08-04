# memory_manager.py
# Saeed Core v6.3
# Smart Memory Manager


import sqlite3
import datetime


DATABASE = "saeed_memory.db"





def connect():

    return sqlite3.connect(DATABASE)





def init_memory_manager():

    conn = connect()
    cursor = conn.cursor()



    cursor.execute("""
        CREATE TABLE IF NOT EXISTS memories(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            content TEXT,

            category TEXT,

            importance INTEGER,

            time TEXT

        )
    """)



    conn.commit()
    conn.close()





def add_memory(
        content,
        category="general",
        importance=1
):


    try:

        conn = connect()
        cursor = conn.cursor()



        cursor.execute(
            """
            INSERT INTO memories(
                content,
                category,
                importance,
                time
            )

            VALUES (?,?,?,?)
            """,

            (

                content,

                category,

                importance,

                str(datetime.datetime.now())

            )
        )



        conn.commit()
        conn.close()



        return True



    except Exception as e:


        print(
            "Add memory error:",
            e
        )


        return False







def get_all_memories():


    conn = connect()
    cursor = conn.cursor()



    cursor.execute(
        """
        SELECT *

        FROM memories

        ORDER BY importance DESC
        """
    )



    result = cursor.fetchall()



    conn.close()



    return result







def get_best_memory(keyword):


    conn = connect()
    cursor = conn.cursor()



    cursor.execute(

        """
        SELECT content

        FROM memories

        WHERE content LIKE ?

        ORDER BY importance DESC

        LIMIT 5
        """,

        (
            "%" + keyword + "%",
        )

    )



    result = cursor.fetchall()



    conn.close()



    return result
