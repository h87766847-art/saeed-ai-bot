# planner_intelligence.py
# Saeed Core
# Advanced Planning Intelligence System


import datetime
import json





PLANS_DATABASE = []







def create_plan(

        title,

        steps,

        priority="normal"

):


    plan = {


        "id":

        len(PLANS_DATABASE) + 1,


        "title":

        title,


        "steps":

        steps,


        "priority":

        priority,


        "status":

        "active",


        "created":

        str(
            datetime.datetime.now()
        )

    }



    PLANS_DATABASE.append(

        plan

    )



    return plan







def get_active_plans():


    active = []



    for plan in PLANS_DATABASE:


        if plan["status"] == "active":


            active.append(

                plan

            )



    return active







def complete_plan(

        plan_id

):


    for plan in PLANS_DATABASE:


        if plan["id"] == plan_id:


            plan["status"] = "completed"


            return True



    return False







def analyze_plan_request(

        text

):


    keywords = [

        "برنامه",

        "هدف",

        "مرحله",

        "شروع",

        "پروژه"

    ]



    score = 0



    for word in keywords:


        if word in text:


            score += 1






    return {


        "is_planning": score > 0,


        "confidence": score

    }







def export_plans():


    return json.dumps(

        PLANS_DATABASE,

        ensure_ascii=False,

        indent=2

    )







def clear_completed_plans():


    global PLANS_DATABASE



    PLANS_DATABASE = [

        p for p in PLANS_DATABASE

        if p["status"] != "completed"

    ]
