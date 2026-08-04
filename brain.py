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



# شروع مدیریت حافظه
init_memory_manager()



def connect():
    return sqlite3.connect(DATABASE)



def save_brain_log(text):

    try:
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



def process_brain(text, context=None, memory=None, plans=None, decisions=None):

    # تشخیص موضوع گفتگو
    detected_context = detect_context(text)


    # تحلیل حافظه
    try:
        memory_result = analyze_memory(text)
    except Exception:
        memory_result = None


    # ذخیره در حافظه
    try:
        add_memory(text)
    except Exception:
        pass


    # ثبت لاگ
    save_brain_log(text)



    response = {
        "input": text,
        "context": detected_context,
        "memory": memory_result,
        "plans": plans,
        "decisions": decisions,
        "time": str(datetime.datetime.now()),
        "status": "success"
    }


    return response
