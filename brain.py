# brain.py
# Saeed Core
# Central Intelligence Brain System


import datetime


# اتصال امن به سیستم‌ها

try:
    from memory_manager import (
        add_memory,
        get_best_memory
    )
except Exception:
    add_memory = None
    get_best_memory = None


try:
    from context_intelligence import (
        detect_context
    )
except Exception:
    detect_context = None


try:
    from intent_engine import (
        detect_intent
    )
except Exception:
    detect_intent = None


try:
    from learning_engine import (
        add_experience
    )
except Exception:
    add_experience = None


try:
    from event_engine import (
        emit_event
    )
except Exception:
    emit_event = None


try:
    from identity_engine import (
        get_identity
    )
except Exception:
    get_identity = None





BRAIN_VERSION = "7.0"





CONVERSATIONS = []








def init_database():

    """
    سازگاری با فایل‌های قدیمی
    """

    return True








def save_conversation(

        user_text,

        response

):


    data = {

        "user":

        user_text,


        "response":

        response,


        "time":

        str(

            datetime.datetime.now()

        )

    }


    CONVERSATIONS.append(

        data

    )


    return data







def remember_important_information(

        information

):


    if add_memory:


        try:

            return add_memory(

                information

            )

        except Exception:

            pass


    return False







def analyze_input(

        text

):


    result = {


        "text":

        text,


        "time":

        str(

            datetime.datetime.now()

        )

    }



    if detect_context:


        try:

            result["context"] = detect_context(

                text

            )

        except Exception:

            result["context"] = None




    if detect_intent:


        try:

            result["intent"] = detect_intent(

                text

            )

        except Exception:

            result["intent"] = None




    return result







def process_brain(

        text

):


    analysis = analyze_input(

        text

    )



    if add_experience:


        try:

            add_experience(

                text,

                "processing",

                "completed",

                1

            )

        except Exception:

            pass




    if emit_event:


        try:

            emit_event(

                "brain_processed",

                analysis

            )

        except Exception:

            pass




    response = {


        "status":

        "success",


        "version":

        BRAIN_VERSION,


        "analysis":

        analysis,


        "message":

        "Request processed by Saeed Core"

    }





    save_conversation(

        text,

        response

    )



    return response







def get_brain_status():


    return {


        "name":

        "Saeed Brain",


        "version":

        BRAIN_VERSION,


        "conversations":

        len(CONVERSATIONS),


        "status":

        "online"

    }
