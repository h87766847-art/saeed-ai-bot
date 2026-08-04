# learning_engine.py
# Saeed Core
# Advanced Learning Engine


import sqlite3
import datetime
import json



DATABASE = "saeed_memory.db"






def connect():

    return sqlite3.connect(
        DATABASE
    )








def init_learning_engine():


    conn = connect()

    cursor = conn.cursor()



    cursor.execute("""
    CREATE TABLE IF NOT EXISTS learning_data(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        input TEXT,

        output TEXT,

        feedback TEXT,

        score INTEGER DEFAULT 0,

        tags TEXT,

        created TEXT

    )
    """)



    conn.commit()

    conn.close()







def save_experience(

        user_input,

        output,

        feedback=None,

        score=0,

        tags=None

):


    try:


        if tags is None:

            tags = []



        conn = connect()

        cursor = conn.cursor()



        cursor.execute(
        """

        INSERT INTO learning_data

        (

        input,

        output,

        feedback,

        score,

        tags,

        created

        )


        VALUES (?,?,?,?,?,?)

        """,

        (

        user_input,

        output,

        feedback,

        score,

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

            "Learning save error:",

            e

        )


        return False








def get_learning_history(

        limit=20

):


    conn = connect()

    cursor = conn.cursor()



    cursor.execute(

    """

    SELECT *

    FROM learning_data

    ORDER BY id DESC

    LIMIT ?

    """,

    (

    limit,

    ))



    result = cursor.fetchall()



    conn.close()



    return result








def rate_experience(

        experience_id,

        score

):


    conn = connect()

    cursor = conn.cursor()



    cursor.execute(

    """

    UPDATE learning_data

    SET score=?

    WHERE id=?

    """,

    (

    score,

    experience_id

    ))



    conn.commit()

    conn.close()








def analyze_learning():


    data = get_learning_history()



    total = len(data)



    if total == 0:


        return {


            "status":

            "empty",


            "total":

            0

        }






    scores = []



    for item in data:


        scores.append(

            item[4]

        )





    average = sum(scores) / total






    return {


        "status":

        "active",


        "experiences":

        total,


        "average_score":

        average

    }








init_learning_engine()
