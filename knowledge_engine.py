# knowledge_engine.py
# Saeed Core
# Advanced Knowledge Management System


import sqlite3
import datetime
import json



DATABASE = "saeed_memory.db"






def connect():

    return sqlite3.connect(
        DATABASE
    )








def init_knowledge_engine():


    conn = connect()

    cursor = conn.cursor()



    cursor.execute("""
    CREATE TABLE IF NOT EXISTS knowledge(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        title TEXT,

        content TEXT,

        category TEXT,

        tags TEXT,

        importance INTEGER DEFAULT 1,

        created TEXT

    )
    """)



    conn.commit()

    conn.close()







def add_knowledge(

        title,

        content,

        category="general",

        tags=None,

        importance=1

):


    try:


        if tags is None:

            tags = []



        conn = connect()

        cursor = conn.cursor()



        cursor.execute(

        """

        INSERT INTO knowledge

        (

        title,

        content,

        category,

        tags,

        importance,

        created

        )

        VALUES (?,?,?,?,?,?)

        """,

        (

        title,

        content,

        category,

        json.dumps(

            tags,

            ensure_ascii=False

        ),

        importance,

        str(

            datetime.datetime.now()

        )

        ))



        conn.commit()

        conn.close()



        return True



    except Exception as e:


        print(

            "Knowledge error:",

            e

        )


        return False







def search_knowledge(

        query,

        limit=10

):


    conn = connect()

    cursor = conn.cursor()



    cursor.execute(

    """

    SELECT *

    FROM knowledge

    WHERE title LIKE ?

    OR content LIKE ?

    ORDER BY importance DESC

    LIMIT ?

    """,

    (

    "%" + query + "%",

    "%" + query + "%",

    limit

    ))



    result = cursor.fetchall()



    conn.close()



    return result







def get_all_knowledge():


    conn = connect()

    cursor = conn.cursor()



    cursor.execute(

    """

    SELECT *

    FROM knowledge

    ORDER BY importance DESC

    """

    )



    result = cursor.fetchall()



    conn.close()



    return result








def knowledge_stats():


    data = get_all_knowledge()



    return {


        "total":

        len(data),


        "status":

        "active"


    }







init_knowledge_engine()
