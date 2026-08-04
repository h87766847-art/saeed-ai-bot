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



# Initialize memory system
init_memory_manager()



def connect():
    return sqlite3.connect(DATABASE)



def init_database():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS brain_logs(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT,
            time TEXT
        )
        """
    )

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



# Create database when module loads
init_database()
