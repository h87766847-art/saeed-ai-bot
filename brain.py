# brain.py
# Saeed Core v6.3
# Brain Intelligence Module


import sqlite3
import datetime


from memory_manager import (
    init_memory_manager,
    add_memory
)


from memory_intelligence import (
    analyze_memory
)


from context_intelligence import (
    detect_context
)



DATABASE = "saeed_memory.db"



# شروع سیستم حافظه
init_memory_manager()



def connect():

    return sqlite3.connect(DATABASE)




def init_database():

    conn = connect()
    cursor = conn.cursor()


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS brain_logs(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT,
            time TEXT
        )
    """)


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversations(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user TEXT,
            assistant TEXT,
            time TEXT
        )
    """)


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS important_information(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            information TEXT,
            time TEXT
        )
    """)


    conn.commit()
    conn.close()




def save_brain_log(text):

    try:

        conn = connect()
        cursor = conn.cursor()


        cursor.execute(
            """
            INSERT INTO brain_logs(message,time)
            VALUES (?,?)
            """,
            (
                text,
                str(datetime.datetime.now())
            )
        )


        conn.commit()
        conn.close()


    except Exception as e:

        print("Brain log error:", e)





def save_conversation(user_text, assistant_text):

    try:

        conn = connect()
        cursor = conn.cursor()


        cursor.execute(
            """
            INSERT INTO conversations(
                user,
                assistant,
                time
            )
            VALUES (?,?,?)
            """,
            (
                user_text,
                assistant_text,
                str(datetime.datetime.now())
            )
        )


        conn.commit()
        conn.close()


    except Exception as e:

        print("Conversation error:", e)





def remember_important_information(information):

    try:

        conn = connect()
        cursor = conn.cursor()


        cursor.execute(
            """
            INSERT INTO important_information(
                information,
                time
            )
            VALUES (?,?)
            """,
            (
                information,
                str(datetime.datetime.now())
            )
        )


        conn.commit()
        conn.close()


        return True


    except Exception as e:

        print("Memory save error:", e)

        return False






def process_brain(
        text,
        context=None,
        memory=None,
        plans=None,
        decisions=None
):


    try:

        detected_context = detect_context(text)

    except Exception:

        detected_context = None



    try:

        memory_result = analyze_memory(text)

    except Exception:

        memory_result = None




    try:

        add_memory(text)

    except Exception:

        pass




    save_brain_log(text)



    return {

        "input": text,

        "context": detected_context,

        "memory": memory_result,

        "plans": plans,

        "decisions": decisions,

        "status": "success",

        "time": str(datetime.datetime.now())

    }





# ساخت دیتابیس هنگام اجرا
init_database()
