# scheduler_upgrade.py
# Saeed Core v10.4
# Upgrade Scheduler System


import datetime





SCHEDULE_LOG = []








def check_upgrade_time(

    system_state="normal",

    priority="medium"

):


    result = {


        "time":

        str(datetime.datetime.now()),


        "system_state":

        system_state,


        "priority":

        priority,


        "decision":

        None

    }







    if system_state == "busy":


        result["decision"] = "delay"






    elif priority == "high":


        result["decision"] = "upgrade_now"






    else:


        result["decision"] = "scheduled"







    SCHEDULE_LOG.append(

        result

    )



    return result









def can_upgrade_now(

    schedule_result

):


    return schedule_result.get(

        "decision"

    ) == "upgrade_now"

    or schedule_result.get(

        "decision"

    ) == "scheduled"









def scheduler_status():


    return {


        "scheduled_checks":

        len(

            SCHEDULE_LOG

        ),


        "status":

        "active"

    }
