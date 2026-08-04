# decision_intelligence.py
# Saeed Core v7.0
# Decision Intelligence System


import datetime
import uuid





DECISIONS = {}







def create_decision(

        question,

        options

):


    decision_id = str(

        uuid.uuid4()

    )



    DECISIONS[decision_id] = {


        "id":

        decision_id,


        "question":

        question,


        "options":

        options,


        "selected":

        None,


        "created":

        str(

            datetime.datetime.now()

        )

    }



    return DECISIONS[decision_id]








def evaluate_option(

        option,

        score

):


    return {


        "option":

        option,


        "score":

        score

    }









def choose_best(

        options

):


    if not options:


        return None



    best = max(

        options,

        key=lambda x: x.get(

            "score",

            0

        )

    )



    return best







def save_decision_result(

        decision_id,

        selected

):


    if decision_id in DECISIONS:


        DECISIONS[decision_id]["selected"] = selected


        DECISIONS[decision_id]["completed"] = str(

            datetime.datetime.now()

        )


        return True



    return False







def get_decisions(

        question=None

):


    if question:


        result = []



        for decision in DECISIONS.values():


            if question.lower() in decision["question"].lower():


                result.append(

                    decision

                )



        return result





    return list(

        DECISIONS.values()

    )







def decision_status():


    return {


        "decisions":

        len(DECISIONS),


        "status":

        "active"

        }
