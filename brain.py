# brain.py
# Saeed Core v6.5
# Smart Brain + Personality + Emotion


import sqlite3
import datetime


from memory_manager import (
    init_memory_manager,
    add_memory
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
    detect_emotion,
    get_emotion_response
)



DATABASE = "saeed_memory.db"




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



    conn.commit()

    conn.close()






def save_brain_log(text):

    try:

        conn = connect()

        cursor = conn.cursor()


        cursor.execute(
            """
            INSERT INTO brain_logs(
                message,
                time
            )
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

        print(
            "Brain log error:",
            e
        )







def save_conversation(
        user_text,
        assistant_text
):

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

        print(
            "Conversation error:",
            e
        )








def remember_important_information(
        information
):

    try:

        add_memory(
            information,
            category="important",
            importance=5
        )


        return True


    except Exception as e:

        print(
            "Memory error:",
            e
        )

        return False







def process_brain(
        text,
        context=None,
        memory=None,
        plans=None,
        decisions=None
):


    # تشخیص موضوع

    try:

        detected_context = detect_context(
            text
        )

    except Exception:

        detected_context = None





    # تشخیص احساس

    emotion = detect_emotion(
        text
    )





    # حافظه

    memory_analysis = analyze_memory(
        text
    )




    if memory_analysis.get(
        "important"
    ):

        remember_important_information(
            text
        )





    information = extract_information(
        text
    )





    personality = get_personality()





    emotional_reply = get_emotion_response(
        emotion["emotion"]
    )





    response = add_personality(
        emotional_reply
    )






    save_brain_log(
        text
    )






    return {


        "input": text,


        "response": response,


        "personality": personality,


        "emotion": emotion,


        "context": detected_context,


        "memory": memory_analysis,


        "information": information,


        "plans": plans,


        "decisions": decisions,


        "status": "success",


        "time": str(
            datetime.datetime.now()
        )

    }







init_database()
