# priority_engine.py
# Saeed Core
# Advanced Priority Management System


import datetime
import uuid





PRIORITIES = {}







def add_priority(

        name,

        description="",

        importance=5,

        urgency=5

):


    priority_id = str(

        uuid.uuid4()

    )



    score = (

        importance * 0.6

    ) + (

        urgency * 0.4

    )



    PRIORITIES[priority_id] = {


        "id":

        priority_id,


        "name":

        name,


        "description":

        description,


        "importance":

        importance,


        "urgency":

        urgency,


        "score":

        score,


        "status":

        "pending",


        "created":

        str(

            datetime.datetime.now()

        )

    }



    return PRIORITIES[priority_id]








def calculate_priority(

        importance,

        urgency

):


    return (

        importance * 0.6

    ) + (

        urgency * 0.4

    )









def get_top_priorities(

        limit=10

):


    data = list(

        PRIORITIES.values()

    )



    data.sort(

        key=lambda x: x["score"],

        reverse=True

    )



    return data[:limit]









def complete_priority(

        priority_id

):


    if priority_id in PRIORITIES:


        PRIORITIES[priority_id]["status"] = "completed"


        return True



    return False








def remove_priority(

        priority_id

):


    if priority_id in PRIORITIES:


        del PRIORITIES[priority_id]


        return True



    return False








def priority_status():


    return {


        "total":

        len(PRIORITIES),


        "pending":

        len(

            [

            x for x in PRIORITIES.values()

            if x["status"] == "pending"

            ]

        ),


        "status":

        "active"

    }
