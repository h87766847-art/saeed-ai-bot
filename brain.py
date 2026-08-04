# brain.py
# Saeed Core
# Advanced Brain Engine


import sqlite3
import datetime
import json
import traceback



from memory_manager import (
    init_memory_manager,
    add_memory,
    get_best_memory
)


from memory_intelligence import (
    analyze_memory,
    extract_information
)


from context_intelligence import (
    detect_context
)


from personality_engine import (
    get_personality,
    add_personality
)


from emotion_engine import (
    detect_emotion
)


from decision_intelligence import (
    get_decision
)



DATABASE = "saeed_memory.db"



# -----------------------------
# Initialization
# -----------------------------


init_memory_manager()






def connect():

    return sqlite3.connect(
        DATABASE
    )







def init_database():

    conn = connect()

    cursor = conn.cursor()



    cursor.execute("""
    CREATE TABLE IF NOT EXISTS brain_logs(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        input TEXT,

        output TEXT,

        data TEXT,

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



    conn.commit()

    conn.close()







# -----------------------------
# Logging
# -----------------------------


def save_log(
        user_input,
        output,
        data
):

    try:

        conn = connect()

        cursor = conn.cursor()



        cursor.execute(
        """
        INSERT INTO brain_logs
        (
        input,
        output,
        data,
        time
        )

        VALUES (?,?,?,?)
        """,

        (

        user_input,

        output,

        json.dumps(
            data,
            ensure_ascii=False
        ),

        str(
            datetime.datetime.now()
        )

        ))



        conn.commit()

        conn.close()



    except Exception:

        traceback.print_exc()







def save_conversation(
        user,
        assistant
):

    try:

        conn = connect()

        cursor = conn.cursor()


        cursor.execute(
        """
        INSERT INTO conversations
        (
        user,
        assistant,
        time
        )

        VALUES (?,?,?)
        """,

        (

        user,

        assistant,

        str(
            datetime.datetime.now()
        )

        ))


        conn.commit()

        conn.close()



    except Exception:

        traceback.print_exc()








# -----------------------------
# Memory
# -----------------------------


def remember(
        text,
        importance=5
):

    try:

        add_memory(

            text,

            category="brain",

            importance=importance

        )


        return True



    except Exception:

        return False








# -----------------------------
# Main Brain
# -----------------------------


def process_brain(
        text,
        context=None,
        memory=None,
        plans=None,
        decisions=None
):


    result = {}



    try:


        result["input"] = text



        # Context

        result["context"] = detect_context(
            text
        )



        # Emotion

        result["emotion"] = detect_emotion(
            text
        )



        # Decision

        result["decision"] = get_decision(
            text
        )



        # Memory analysis

        memory_info = analyze_memory(
            text
        )


        result["memory_analysis"] = memory_info




        # Extract information

        result["information"] = extract_information(
            text
        )




        # Important memory save

        if memory_info.get(
            "important",
            False
        ):


            remember(
                text,

                memory_info.get(
                    "importance_score",
                    5
                )

            )





        # Related memories

        result["related_memory"] = get_best_memory(
            text
        )





        # Personality

        result["personality"] = get_personality()





        # Internal response layer

        response = add_personality(
            "درخواست شما پردازش شد."
        )



        result["response"] = response



        result["status"] = "success"




    except Exception as e:


        result = {

            "status": "error",

            "error": str(e),

            "trace":
            traceback.format_exc()

        }




    save_log(

        text,

        result.get(
            "response",
            ""
        ),

        result

    )



    return result







# Start database

init_database()
