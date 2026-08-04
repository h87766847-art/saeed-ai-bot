# goal_engine.py
# Saeed Core
# Advanced Goal Management System


import datetime
import uuid





GOALS = {}







def create_goal(

        title,

        description="",

        priority="normal"

):


    goal_id = str(

        uuid.uuid4()

    )



    GOALS[goal_id] = {


        "id":

        goal_id,


        "title":

        title,


        "description":

        description,


        "priority":

        priority,


        "progress":

        0,


        "status":

        "active",


        "steps":

        [],


        "created":

        str(

            datetime.datetime.now()

        )

    }



    return GOALS[goal_id]








def add_step(

        goal_id,

        step

):


    if goal_id not in GOALS:


        return False




    GOALS[goal_id]["steps"].append(

        {


            "title":

            step,


            "done":

            False

        }

    )



    return True







def complete_step(

        goal_id,

        index

):


    if goal_id not in GOALS:


        return False




    steps = GOALS[goal_id]["steps"]



    if index < len(steps):


        steps[index]["done"] = True



        update_progress(

            goal_id

        )


        return True




    return False








def update_progress(

        goal_id

):


    goal = GOALS.get(

        goal_id

    )



    if not goal:


        return False




    steps = goal["steps"]



    if len(steps) == 0:


        goal["progress"] = 0


        return True






    completed = 0



    for step in steps:


        if step["done"]:


            completed += 1





    goal["progress"] = int(

        (completed / len(steps)) * 100

    )



    if goal["progress"] == 100:


        goal["status"] = "completed"



    return True







def get_active_goals():


    return [

        goal

        for goal in GOALS.values()

        if goal["status"] == "active"

    ]








def get_goal(

        goal_id

):


    return GOALS.get(

        goal_id,

        None

    )







def goal_status():


    return {


        "total":

        len(GOALS),


        "active":

        len(get_active_goals()),


        "status":

        "running"

    }
