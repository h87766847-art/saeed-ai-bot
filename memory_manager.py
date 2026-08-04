# memory_manager.py
# Saeed Core
# Advanced Memory Management System


import sqlite3
import datetime
import json



DATABASE = "saeed_memory.db"





def connect():

    return sqlite3.connect(
        DATABASE
    )








def init_memory_manager():


    conn = connect()

    cursor = conn.cursor()



    cursor.execute("""
    CREATE TABLE IF NOT EXISTS memories(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        content TEXT,

        category TEXT,

        importance INTEGER DEFAULT 1,

        tags TEXT,

        created TEXT,

        accessed INTEGER DEFAULT 0

    )
    """)




    conn.commit()

    conn.close()







def add_memory(

        content,

        category="general",

        importance=1,

        tags=None

):


    try:


        conn = connect()

        cursor = conn.cursor()



        if tags is None:

            tags = []




        cursor.execute(

        """
        INSERT INTO memories

        (
        content,
        category,
        importance,
        tags,
        created
        )

        VALUES (?,?,?,?,?)

        """,

        (

        content,

        category,

        importance,

        json.dumps(
            tags,
            ensure_ascii=False
        ),

        str(
            datetime.datetime.now()
        )

        ))





        conn.commit()

        conn.close()



        return True



    except Exception as e:


        print(
            "Memory save error:",
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







def get_best_memory(

        keyword,

        limit=10

):


    conn = connect()

    cursor = conn.cursor()



    cursor.execute(

    """

    SELECT content

    FROM memories

    WHERE content LIKE ?

    ORDER BY importance DESC

    LIMIT ?

    """,

    (

    "%" + keyword + "%",

    limit

    ))



    result = cursor.fetchall()



    conn.close()



    return result







def delete_memory(

        memory_id

):


    conn = connect()

    cursor = conn.cursor()



    cursor.execute(

    """

    DELETE FROM memories

    WHERE id=?

    """,

    (

    memory_id,

    ))



    conn.commit()

    conn.close()






def increase_memory_usage(

        memory_id

):


    conn = connect()

    cursor = conn.cursor()



    cursor.execute(

    """

    UPDATE memories

    SET accessed = accessed + 1

    WHERE id=?

    """,

    (

    memory_id,

    ))



    conn.commit()

    conn.close()






def search_memory(

        text

):


    words = text.split()



    results = []



    for word in words:


        found = get_best_memory(
            word,
            5
        )


        results.extend(
            found
        )



    return results
