# autonomous_engine.py
# Saeed Core
# Advanced Autonomous Task Engine


import datetime
import uuid





TASKS = {}







def create_task(

        name,

        action,

        priority="normal"

):


    task_id = str(

        uuid.uuid4()

    )



    TASKS[task_id] = {


        "id":

        task_id,


        "name":

        name,


        "action":

        action,


        "priority":

        priority,


        "status":

        "pending",


        "created":

        str(

            datetime.datetime.now()

        )

    }



    return TASKS[task_id]








def run_task(

        task_id

):


    task = TASKS.get(

        task_id

    )



    if not task:


        return {


            "status":

            "error",


            "message":

            "task not found"

        }






    try:


        result = task["action"]()



        task["status"] = "completed"



        task["result"] = result




        return {


            "status":

            "success",


            "result":

            result

        }





    except Exception as e:



        task["status"] = "failed"



        task["error"] = str(e)



        return {


            "status":

            "error",


            "error":

            str(e)

        }








def get_tasks():


    return list(

        TASKS.values()

    )







def get_pending_tasks():


    return [

        task

        for task in TASKS.values()

        if task["status"] == "pending"

    ]








def cancel_task(

        task_id

):


    if task_id in TASKS:


        TASKS[task_id]["status"] = "cancelled"


        return True



    return False 






def autonomous_status():


    return {


        "total_tasks":

        len(TASKS),


        "pending":

        len(get_pending_tasks()),


        "status":

        "active"

    }
