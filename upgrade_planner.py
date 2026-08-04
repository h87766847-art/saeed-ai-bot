# upgrade_planner.py
# Saeed Core
# Advanced Upgrade Planning System


import datetime
import uuid





UPGRADE_PLANS = {}







def create_upgrade_plan(

        title,

        description,

        priority=5

):


    plan_id = str(

        uuid.uuid4()

    )



    UPGRADE_PLANS[plan_id] = {


        "id":

        plan_id,


        "title":

        title,


        "description":

        description,


        "priority":

        priority,


        "status":

        "pending",


        "created":

        str(

            datetime.datetime.now()

        )

    }



    return UPGRADE_PLANS[plan_id]








def get_upgrade_plans():


    plans = list(

        UPGRADE_PLANS.values()

    )



    plans.sort(

        key=lambda x: x["priority"],

        reverse=True

    )



    return plans







def approve_upgrade(

        plan_id

):


    if plan_id in UPGRADE_PLANS:


        UPGRADE_PLANS[plan_id]["status"] = "approved"


        return True



    return False







def complete_upgrade(

        plan_id

):


    if plan_id in UPGRADE_PLANS:


        UPGRADE_PLANS[plan_id]["status"] = "completed"


        return True



    return False







def remove_upgrade_plan(

        plan_id

):


    if plan_id in UPGRADE_PLANS:


        del UPGRADE_PLANS[plan_id]


        return True



    return False







def upgrade_planner_status():


    return {


        "plans":

        len(UPGRADE_PLANS),


        "pending":

        len(

            [

            x for x in UPGRADE_PLANS.values()

            if x["status"] == "pending"

            ]

        ),


        "status":

        "active"

    }
