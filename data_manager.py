# data_manager.py
# Saeed Core
# Advanced Data Management System


import sqlite3
import json
import datetime



DATABASE = "saeed_core_data.db"







def connect():

    return sqlite3.connect(
        DATABASE
    )








def init_database():


    conn = connect()

    cursor = conn.cursor()



    cursor.execute("""
    CREATE TABLE IF NOT EXISTS core_data(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        data_key TEXT UNIQUE,

        data_value TEXT,

        category TEXT,

        created TEXT,

        updated TEXT

    )
    """)



    conn.commit()

    conn.close()







def save_data(

        key,

        value,

        category="general"

):


    conn = connect()

    cursor = conn.cursor()



    now = str(

        datetime.datetime.now()

    )



    cursor.execute(

    """

    INSERT OR REPLACE INTO core_data

    (

    data_key,

    data_value,

    category,

    created,

    updated

    )

    VALUES (?,?,?,?,?)

    """,

    (

    key,

    json.dumps(

        value,

        ensure_ascii=False

    ),

    category,

    now,

    now

    ))



    conn.commit()

    conn.close()



    return True







def load_data(

        key

):


    conn = connect()

    cursor = conn.cursor()



    cursor.execute(

    """

    SELECT data_value

    FROM core_data

    WHERE data_key=?

    """,

    (

    key,

    ))



    result = cursor.fetchone()



    conn.close()



    if result:


        return json.loads(

            result[0]

        )



    return None








def delete_data(

        key

):


    conn = connect()

    cursor = conn.cursor()



    cursor.execute(

    """

    DELETE FROM core_data

    WHERE data_key=?

    """,

    (

    key,

    ))



    conn.commit()

    conn.close()



    return True







def get_all_data():


    conn = connect()

    cursor = conn.cursor()



    cursor.execute(

    """

    SELECT *

    FROM core_data

    ORDER BY id DESC

    """

    )



    result = cursor.fetchall()



    conn.close()



    return result







def data_status():


    data = get_all_data()



    return {


        "items":

        len(data),


        "database":

        DATABASE,


        "status":

        "active"

    }







init_database()
