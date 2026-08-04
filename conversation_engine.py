# conversation_engine.py
# Saeed Core
# Advanced Conversation Management System


import datetime
import uuid





CONVERSATIONS = {}







def create_session(

        user_id

):


    session_id = str(

        uuid.uuid4()

    )



    CONVERSATIONS[session_id] = {


        "user_id":

        user_id,


        "messages":

        [],


        "created":

        str(

            datetime.datetime.now()

        ),


        "last_activity":

        str(

            datetime.datetime.now()

        )

    }




    return session_id







def add_message(

        session_id,

        role,

        content

):


    if session_id not in CONVERSATIONS:


        return False






    CONVERSATIONS[session_id]["messages"].append(

        {


            "role":

            role,


            "content":

            content,


            "time":

            str(

                datetime.datetime.now()

            )

        }

    )



    CONVERSATIONS[session_id]["last_activity"] = str(

        datetime.datetime.now()

    )



    return True







def get_history(

        session_id,

        limit=20

):


    if session_id not in CONVERSATIONS:


        return []





    return CONVERSATIONS[session_id]["messages"][-limit:]









def get_session_info(

        session_id

):


    return CONVERSATIONS.get(

        session_id,

        None

    )








def clear_session(

        session_id

):


    if session_id in CONVERSATIONS:


        del CONVERSATIONS[session_id]


        return True



    return False







def conversation_status():


    return {


        "active_sessions":

        len(CONVERSATIONS),


        "status":

        "online"

    }
