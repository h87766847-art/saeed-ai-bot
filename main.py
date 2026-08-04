# main.py
# Saeed Core repaired version

import datetime


try:
    from core_router import route_message
except Exception:
    route_message = None


try:
    from core_manager import register_component, core_status
except Exception:
    register_component = None
    core_status = None


try:
    from module_loader import load_all_modules, loader_status
except Exception:
    load_all_modules = None
    loader_status = None


SYSTEM_NAME = "Saeed Core"
VERSION = "7.5"


def initialize_system():

    if load_all_modules:
        try:
            load_all_modules()
        except Exception as e:
            print("Module load error:", e)


    if register_component:
        try:
            register_component("main", "active")
            register_component("router", "active")
        except Exception:
            pass


    return True



def process_message(message):

    try:

        if route_message:
            return route_message(message)

        return "Router not available"

    except Exception as e:

        return {
            "status": "error",
            "message": str(e)
        }



def system_status():

    data = {
        "name": SYSTEM_NAME,
        "version": VERSION,
        "time": str(datetime.datetime.now())
    }


    if core_status:
        try:
            data["core"] = core_status()
        except:
            pass


    if loader_status:
        try:
            data["modules"] = loader_status()
        except:
            pass


    return data



def start():

    initialize_system()

    print("Saeed Core started")
    print(system_status())



if __name__ == "__main__":

    start()

    print("Saeed Core running...")
