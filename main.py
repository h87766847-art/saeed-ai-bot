# main.py
# Saeed Core v7.5
# Main System Controller


import datetime


from core_router import route_message



try:
    from core_manager import (
        register_component,
        core_status
    )

except Exception:

    register_component = None
    core_status = None



try:
    from module_loader import (
        load_all_modules,
        loader_status
    )

except Exception:

    load_all_modules = None
    loader_status = None



try:
    from self_diagnosis_engine import (
        diagnosis_status
    )

except Exception:

    diagnosis_status = None





SYSTEM_NAME = "Saeed Core"

VERSION = "7.5"





def initialize_system():


    if load_all_modules:

        try:
            load_all_modules()

        except Exception:
            pass



    if register_component:

        try:

            register_component(
                "main",
                "active"
            )


            register_component(
                "router",
                "active"
            )


        except Exception:
            pass



    return True






def process_message(message):

    try:

        return route_message(
            message
        )


    except Exception as e:

        return {

            "status": "error",

            "message": str(e)

        }








def system_status():

    status = {

        "name": SYSTEM_NAME,

        "version": VERSION,

        "time": str(
            datetime.datetime.now()
        )

    }



    if core_status:

        status["core"] = core_status()



    if loader_status:

        status["modules"] = loader_status()



    if diagnosis_status:

        status["diagnosis"] = diagnosis_status()



    return status








def start():

    initialize_system()


    print(
        SYSTEM_NAME,
        "started"
    )


    print(
        system_status()
    )








if __name__ == "__main__":


    start()


    print(
        "Saeed Core running..."
    )


    # Console input disabled
    # Telegram listener should run here
