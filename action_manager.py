import json
import os
import datetime


FILE = "saeed_tasks.json"



def load_tasks():

    if not os.path.exists(FILE):

        return []


    with open(
        FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)





def save_tasks(tasks):

    with open(
        FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            tasks,
            f,
            ensure_ascii=False,
            indent=4
        )





def create_task(
    title,
    priority="normal"
):

    tasks = load_tasks()


    task = {

        "title": title,

        "priority": priority,

        "status": "pending",

        "created":
        str(datetime.datetime.now())

    }


    tasks.append(task)


    save_tasks(tasks)


    return task





def complete_task(title):

    tasks = load_tasks()


    for task in tasks:

        if task["title"] == title:

            task["status"] = "completed"



    save_tasks(tasks)






def get_pending_tasks():

    tasks = load_tasks()


    return [

        task for task in tasks

        if task["status"] == "pending"

    ]
