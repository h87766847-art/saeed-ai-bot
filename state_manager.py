# state_manager.py
# Saeed Core
# Advanced State Management System


import datetime
import json





STATE = {

    "mode": "normal",

    "active": True,

    "current_task": None,

    "user": None,

    "context": {},

    "last_update": None

}







def set_state(

        key,

        value

):


    STATE[key] = value



    STATE["last_update"] = str(

        datetime.datetime.now()

    )



    return True







def get_state(

        key,

        default=None

):


    return STATE.get(

        key,

        default

    )








def update_context(

        data

):


    STATE["context"] = data



    STATE["last_update"] = str(

        datetime.datetime.now()

    )



    return True







def get_context():


    return STATE.get(

        "context",

        {}

    )








def reset_state():


    global STATE



    STATE = {


        "mode": "normal",

        "active": True,

        "current_task": None,

        "user": None,

        "context": {},

        "last_update": str(

            datetime.datetime.now()

        )

    }



    return True







def export_state():


    return json.dumps(

        STATE,

        ensure_ascii=False,

        indent=4

    )








def state_status():


    return {


        "active":

        STATE["active"],


        "mode":

        STATE["mode"],


        "last_update":

        STATE["last_update"],


        "status":

        "running"

    }
