# learning_engine.py
# Saeed Core
# Advanced Learning System


import datetime
import uuid





EXPERIENCES = {}







def add_experience(

        situation,

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


        "situation":

        situation,


        "action":

        action,


        "result":

        result,


        "score":

        score,


        "created":

        str(

            datetime.datetime.now()

        )

    }



    return EXPERIENCES[experience_id]








def get_experiences(

        limit=50

):


    data = list(

        EXPERIENCES.values()

    )



    return data[-limit:]








def find_similar(

        situation

):


    results = []



    words = situation.lower().split()



    for exp in EXPERIENCES.values():


        text = exp["situation"].lower()



        matches = 0



        for word in words:


            if word in text:


                matches += 1




        if matches > 0:


            results.append(

                {


                    "experience":

                    exp,


                    "similarity":

                    matches

                }

            )



    results.sort(

        key=lambda x: x["similarity"],

        reverse=True

    )



    return results







def improve_experience(

        experience_id,

        new_score

):


    if experience_id in EXPERIENCES:


        EXPERIENCES[experience_id]["score"] = new_score


        return True



    return False







def learning_report():


    total = len(

        EXPERIENCES

    )



    average = 0



    if total > 0:


        average = sum(

            x["score"]

            for x in EXPERIENCES.values()

        ) / total





    return {


        "experiences":

        total,


        "average_score":

        average,


        "status":

        "learning"

        }
