import sqlite3
import math


DATABASE = "saeed_memory.db"



def connect():

    return sqlite3.connect(
        DATABASE
    )



def init_vectors():

    db = connect()

    cursor = db.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vectors (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        text TEXT,

        vector TEXT

    )
    """)


    db.commit()

    db.close()



# تبدیل ساده متن به بردار

def text_to_vector(text):

    words = text.lower().split()


    vector = {}


    for word in words:

        vector[word] = (
            vector.get(word,0)
            +
            1
        )


    return vector



def similarity(v1,v2):

    common = set(v1) & set(v2)


    if not common:

        return 0



    score = sum(
        v1[x]*v2[x]
        for x in common
    )


    return score





def save_vector(text):

    vector = text_to_vector(
        text
    )


    db = connect()

    cursor = db.cursor()


    cursor.execute(
        """
        INSERT INTO vectors
        (text,vector)

        VALUES (?,?)
        """,

        (
            text,
            str(vector)
        )
    )


    db.commit()

    db.close()



def search_vector(query):

    db = connect()

    cursor = db.cursor()


    cursor.execute(
        """
        SELECT text,vector
        FROM vectors
        """
    )


    data = cursor.fetchall()


    db.close()


    q_vector = text_to_vector(
        query
    )


    results = []


    for text, vector in data:

        stored = eval(vector)


        score = similarity(
            q_vector,
            stored
        )


        results.append(
            (
                score,
                text
            )
        )



    results.sort(
        reverse=True
    )


    return results[:5]
