import sqlite3
import datetime


from memory_manager import (
    init_memory_manager,
    add_memory
)



DATABASE = "saeed_memory.db"



init_memory_manager()





def connect():

    return sqlite3.connect(
        DATABASE
    )






def init_database():

    db = connect()

    cursor = db.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS conversations (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        role TEXT,

        content TEXT,

        time TEXT

    )
    """)


    db.commit()

    db.close()







def save_conversation(role, content):

    db = connect()

    cursor = db.cursor()


    cursor.execute(
        """

        INSERT INTO conversations

        (role,content,time)

        VALUES (?,?,?)

        """,

        (

            role,

            content,

            str(datetime.datetime.now())

        )

    )


    db.commit()

    db.close()







def get_context_messages():


    db = connect()

    cursor = db.cursor()


    cursor.execute(
        """

        SELECT role,content

        FROM conversations

        ORDER BY id DESC

        LIMIT 10

        """
    )


    rows = cursor.fetchall()


    db.close()


    messages = []



    for role,content in reversed(rows):

        messages.append(

            {

                "role":role,

                "content":content

            }

        )


    return messages







def remember_important_information(text):


    lower = text.lower()



    if "من" in text:


        add_memory(

            "user",

            text

        )




    if "پروژه" in text:


        add_memory(

            "projects",

            text

        )





    if "دوست دارم" in text or "علاقه" in text:


        add_memory(

            "preferences",

            text

        )





    if "هدف" in text:


        add_memory(

            "goals",

            text

        )









def build_memory_context():


    db = connect()

    cursor = db.cursor()


    cursor.execute(

        """

        SELECT role,content

        FROM conversations

        ORDER BY id DESC

        LIMIT 5

        """

    )


    data = cursor.fetchall()


    db.close()



    result = ""


    for role,content in reversed(data):

        result += (

            role

            +

            ": "

            +

            content

            +

            "\n"

        )



    return result
