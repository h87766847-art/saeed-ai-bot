# learning_engine.py
# Saeed Core v7.5
# Adaptive Learning Engine


import datetime
import uuid





try:

    from event_engine import emit_event

except Exception:

    emit_event = None





EXPERIENCES = {}







def add_experience(

        input_data,

        action,

        result,

        score=1

):


    experience_id = str(

        uuid.uuid4()

    )



    EXPERIENCES[experience_id] = {


        "id":

        experience_id,


        "input":

        input_data,


        "action":

        action,


        "result":

        result,


        "score":

        score,


        "time":

        str(

            datetime.datetime.now()

        )

    }



    if emit_event:


        try:

            emit_event(

                "learning_experience",

                EXPERIENCES[experience_id]

            )

        except Exception:

            pass





    return EXPERIENCES[experience_id]









def get_experiences():


    return list(

        EXPERIENCES.values()

    )









def find_experience(

        keyword

):


    result = []



    for item in EXPERIENCES.values():


        if keyword.lower() in str(item).lower():


            result.append(

                item

            )



    return result







def learning_score():


    if not EXPERIENCES:


        return 0



    total = 0



    for item in EXPERIENCES.values():


        total += item["score"]





    return total / len(

        EXPERIENCES

    )









def learning_status():


    return {


        "experiences":

        len(

            EXPERIENCES

        ),


        "score":

        learning_score(),


        "status":

        "active"

    }
