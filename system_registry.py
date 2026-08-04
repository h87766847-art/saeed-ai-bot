# system_registry.py
# Saeed Core
# Central System Registry


import datetime
import json
import os





REGISTRY_FILE = "saeed_registry.json"







REGISTRY = {

    "modules": {},

    "version": "6.3",

    "created": str(

        datetime.datetime.now()

    )

}







def load_registry():


    global REGISTRY



    if os.path.exists(

        REGISTRY_FILE

    ):


        with open(

            REGISTRY_FILE,

            "r",

            encoding="utf-8"

        ) as file:


            REGISTRY = json.load(

                file

            )



    return REGISTRY







def save_registry():


    with open(

        REGISTRY_FILE,

        "w",

        encoding="utf-8"

    ) as file:


        json.dump(

            REGISTRY,

            file,

            ensure_ascii=False,

            indent=4

        )







def register_module(

        name,

        version="1.0",

        description=""

):


    REGISTRY["modules"][name] = {


        "version":

        version,


        "description":

        description,


        "status":

        "active",


        "registered":

        str(

            datetime.datetime.now()

        )

    }



    save_registry()



    return True







def update_module_status(

        name,

        status

):


    if name in REGISTRY["modules"]:


        REGISTRY["modules"][name]["status"] = status



        save_registry()



        return True



    return False







def get_module(

        name

):


    return REGISTRY["modules"].get(

        name,

        None

    )







def get_all_modules():


    return REGISTRY["modules"]







def system_report():


    return {


        "version":

        REGISTRY["version"],


        "modules":

        len(

            REGISTRY["modules"]

        ),


        "status":

        "registered",


        "time":

        str(

            datetime.datetime.now()

        )

    }







load_registry()
