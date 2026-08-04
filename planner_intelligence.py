# planner_intelligence.py
# Saeed Core v7.0
# Planning Intelligence System


import datetime
import uuid





PLANS = {}







def create_plan(

        title,

        description="",

        priority=5

):


    plan_id = str(

        uuid.uuid4()

    )



    PLANS[plan_id] = {


        "id":

        plan_id,


        "title":

        title,


        "description":

        description,


        "priority":

        priority,


        "status":

        "active",


        "created":

        str(

            datetime.datetime.now()

        )

    }



    return PLANS[plan_id]









def get_active_plans():


    plans = []



    for plan in PLANS.values():


        if plan["status"] == "active":


            plans.append(

                plan

            )



    return plans







def complete_plan(

        plan_id

):


    if plan_id in PLANS:


        PLANS[plan_id]["status"] = "completed"


        PLANS[plan_id]["completed"] = str(

            datetime.datetime.now()

        )


        return True



    return False







def remove_plan(

        plan_id

):


    if plan_id in PLANS:


        del PLANS[plan_id]


        return True



    return False







def find_plan(

        title

):


    result = []



    for plan in PLANS.values():


        if title.lower() in plan["title"].lower():


            result.append(

                plan

            )



    return result







def planner_status():


    return {


        "plans":

        len(PLANS),


        "active":

        len(

            get_active_plans()

        ),


        "status":

        "online"

            }
