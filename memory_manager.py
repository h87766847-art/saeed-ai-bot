# memory_manager.py
# Saeed Core v7.0
# Advanced Memory Management System


import sqlite3
import datetime





DATABASE = "saeed_memory.db"







def connect():


    return sqlite3.connect(

        DATABASE

    )







def init_memory_manager():


    db = connect()

    cursor = db.cursor()



    cursor.execute(

        """

        CREATE TABLE IF NOT EXISTS memories

        (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            content TEXT,

            category TEXT,

            importance INTEGER,

            created TEXT

        )

        """

    )



    db.commit()

    db.close()







def add_memory(

        content,

        category="general",

        importance=5

):


    db = connect()

    cursor = db.cursor()



    cursor.execute(

        """

        INSERT INTO memories

        (

            content,

            category,

            importance,

            created

        )

        VALUES (?, ?, ?, ?)

        """,

        (

            content,

            category,

            importance,

            str(

                datetime.datetime.now()

            )

        )

    )



    db.commit()

    db.close()



    return True







def get_all_memory():


    db = connect()

    cursor = db.cursor()



    cursor.execute(

        """

        SELECT *

        FROM memories

        ORDER BY importance DESC

        """

    )



    result = cursor.fetchall()



    db.close()



    return result







def get_best_memory(

        query

):


    db = connect()

    cursor = db.cursor()



    cursor.execute(

        """

        SELECT *

        FROM memories

        WHERE content LIKE ?

        ORDER BY importance DESC

        LIMIT 10

        """,

        (

            "%" + query + "%",

        )

    )



    result = cursor.fetchall()



    db.close()



    return result







def delete_memory(

        memory_id

):


    db = connect()

    cursor = db.cursor()



    cursor.execute(

        """

        DELETE FROM memories

        WHERE id=?

        """,

        (

            memory_id,

        )

    )



    db.commit()

    db.close()



    return True







def memory_status():


    db = connect()

    cursor = db.cursor()



    cursor.execute(

        "SELECT COUNT(*) FROM memories"

    )



    count = cursor.fetchone()[0]



    db.close()



    return {


        "memories":

        count,


        "status":

        "active"

    }







init_memory_manager()
