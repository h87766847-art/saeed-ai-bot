# task_manager.py
# Saeed Core
# Advanced Task Management System


import datetime
import uuid





TASKS = {}







def create_task(

        title,

        description="",

        priority=5

):


    task_id = str(

        uuid.uuid4()

    )



    TASKS[task_id] = {


        "id":

        task_id,


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



    return TASKS[task_id]









def get_tasks():


    tasks = list(

        TASKS.values()

    )



    tasks.sort(

        key=lambda x: x["priority"],

        reverse=True

    )



    return tasks







def complete_task(

        task_id

):


    if task_id in TASKS:


        TASKS[task_id]["status"] = "completed"


        TASKS[task_id]["completed_at"] = str(

            datetime.datetime.now()

        )


        return True



    return False







def delete_task(

        task_id

):


    if task_id in TASKS:


        del TASKS[task_id]


        return True



    return False







def find_task(

        title

):


    results = []



    for task in TASKS.values():


        if title.lower() in task["title"].lower():


            results.append(

                task

            )



    return results







def task_status():


    return {


        "total":

        len(TASKS),


        "active":

        len(

            [

            x for x in TASKS.values()

            if x["status"] == "pending"

            ]

        ),


        "status":

        "running"

}
