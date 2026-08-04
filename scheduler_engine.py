# scheduler_engine.py
# Saeed Core
# Advanced Scheduler Engine


import datetime
import uuid





SCHEDULES = {}







def create_schedule(

        name,

        task,

        interval="daily"

):


    schedule_id = str(

        uuid.uuid4()

    )



    SCHEDULES[schedule_id] = {


        "id":

        schedule_id,


        "name":

        name,


        "task":

        task,


        "interval":

        interval,


        "status":

        "active",


        "created":

        str(

            datetime.datetime.now()

        ),


        "last_run":

        None

    }



    return SCHEDULES[schedule_id]








def run_schedule(

        schedule_id

):


    schedule = SCHEDULES.get(

        schedule_id

    )



    if not schedule:


        return {


            "status":

            "error",


            "message":

            "schedule not found"

        }






    try:


        result = schedule["task"]()



        schedule["last_run"] = str(

            datetime.datetime.now()

        )



        return {


            "status":

            "success",


            "result":

            result

        }





    except Exception as e:



        return {


            "status":

            "error",


            "error":

            str(e)

        }








def get_schedules():


    return list(

        SCHEDULES.values()

    )







def remove_schedule(

        schedule_id

):


    if schedule_id in SCHEDULES:


        del SCHEDULES[schedule_id]


        return True



    return False







def scheduler_status():


    return {


        "total":

        len(SCHEDULES),


        "active":

        len(

            [

            x for x in SCHEDULES.values()

            if x["status"] == "active"

            ]

        ),


        "status":

        "running"

    }
