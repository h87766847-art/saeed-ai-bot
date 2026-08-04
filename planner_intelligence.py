# planner_intelligence.py
# Saeed AI v2.7
# Goal Planning System


import json
import os
import datetime





PLAN_FILE = "saeed_plans.json"








def load_plans():


    if not os.path.exists(PLAN_FILE):

        return []



    with open(

        PLAN_FILE,

        "r",

        encoding="utf-8"

    ) as file:


        return json.load(file)








def save_plans(plans):


    with open(

        PLAN_FILE,

        "w",

        encoding="utf-8"

    ) as file:


        json.dump(

            plans,

            file,

            ensure_ascii=False,

            indent=4

        )









def create_plan(

    goal,

    steps

):


    plans = load_plans()



    plan = {


        "goal": goal,


        "steps": steps,


        "status": "active",


        "created":

        str(datetime.datetime.now())


    }




    plans.append(

        plan

    )



    save_plans(

        plans

    )



    return plan









def get_active_plans():


    plans = load_plans()



    return [

        plan

        for plan in plans

        if plan.get(

            "status"

        )

        ==

        "active"

    ]









def complete_plan(goal):


    plans = load_plans()



    for plan in plans:


        if plan.get(

            "goal"

        )

        == goal:


            plan["status"] = "completed"





    save_plans(

        plans

    )



    return plans
