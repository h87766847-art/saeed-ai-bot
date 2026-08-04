# self_monitor_engine.py
# Saeed Core
# Advanced Self Monitoring System


import datetime
import traceback





SYSTEM_STATUS = {

    "brain": True,

    "memory": True,

    "learning": True,

    "knowledge": True,

    "personality": True,

    "router": True

}







ERROR_LOG = []








def check_component(

        name,

        status

):


    SYSTEM_STATUS[name] = status



    return {


        "component":

        name,


        "status":

        status

    }









def report_error(

        component,

        error

):


    data = {


        "component":

        component,


        "error":

        str(error),


        "time":

        str(

            datetime.datetime.now()

        ),


        "trace":

        traceback.format_exc()

    }



    ERROR_LOG.append(

        data

    )



    SYSTEM_STATUS[component] = False



    return data







def get_system_status():


    healthy = []

    failed = []



    for key, value in SYSTEM_STATUS.items():


        if value:

            healthy.append(key)

        else:

            failed.append(key)





    return {


        "online":

        len(failed) == 0,


        "healthy":

        healthy,


        "failed":

        failed,


        "time":

        str(

            datetime.datetime.now()

        )

    }








def get_error_history():


    return ERROR_LOG







def repair_component(

        name

):


    SYSTEM_STATUS[name] = True



    return {


        "component":

        name,


        "repaired":

        True

    }
