# capability_manager.py
# Saeed Core v7.5
# Capability Management System


import datetime
import json
import os





CAPABILITY_FILE = "saeed_capabilities.json"


CAPABILITIES = {}







def load_capabilities():


    global CAPABILITIES



    if os.path.exists(

        CAPABILITY_FILE

    ):


        try:


            with open(

                CAPABILITY_FILE,

                "r",

                encoding="utf-8"

            ) as file:


                CAPABILITIES = json.load(

                    file

                )



        except Exception:


            CAPABILITIES = {}



    return CAPABILITIES







def save_capabilities():


    with open(

        CAPABILITY_FILE,

        "w",

        encoding="utf-8"

    ) as file:


        json.dump(

            CAPABILITIES,

            file,

            ensure_ascii=False,

            indent=4

        )









def add_capability(

        name,

        description=""

):


    CAPABILITIES[name] = {


        "description":

        description,


        "enabled":

        True,


        "created":

        str(

            datetime.datetime.now()

        )

    }



    save_capabilities()



    return True







def enable_capability(

        name

):


    if name in CAPABILITIES:


        CAPABILITIES[name]["enabled"] = True


        save_capabilities()


        return True



    return False







def disable_capability(

        name

):


    if name in CAPABILITIES:


        CAPABILITIES[name]["enabled"] = False


        save_capabilities()


        return True



    return False







def get_capabilities():


    return CAPABILITIES







def get_active_capabilities():


    return [

        item

        for item in CAPABILITIES.values()

        if item["enabled"]

    ]









def capability_status():


    return {


        "total":

        len(CAPABILITIES),


        "active":

        len(

            get_active_capabilities()

        ),


        "status":

        "online"

    }







load_capabilities()
