# module_loader.py
# Saeed Core
# Automatic Module Loader System


import os
import importlib
import datetime





LOADED_MODULES = {}







IGNORE_FILES = [

    "__init__.py",

    "module_loader.py"

]







def find_modules(

        folder="."

):


    modules = []



    for file in os.listdir(

        folder

    ):


        if file.endswith(

            ".py"

        ):


            if file not in IGNORE_FILES:


                name = file[:-3]


                modules.append(

                    name

                )



    return modules







def load_module(

        module_name

):


    try:


        module = importlib.import_module(

            module_name

        )



        LOADED_MODULES[module_name] = {


            "status":

            "loaded",


            "module":

            module,


            "time":

            str(

                datetime.datetime.now()

            )

        }



        return True




    except Exception as e:



        LOADED_MODULES[module_name] = {


            "status":

            "failed",


            "error":

            str(e),


            "time":

            str(

                datetime.datetime.now()

            )

        }



        return False







def load_all_modules(

        folder="."

):


    modules = find_modules(

        folder

    )



    results = {}



    for module in modules:


        results[module] = load_module(

            module

        )



    return results








def get_loaded_modules():


    return LOADED_MODULES







def reload_module(

        module_name

):


    try:


        module = importlib.reload(

            LOADED_MODULES[module_name]["module"]

        )



        LOADED_MODULES[module_name]["module"] = module



        LOADED_MODULES[module_name]["time"] = str(

            datetime.datetime.now()

        )



        return True



    except Exception:


        return False







def loader_status():


    return {


        "modules":

        len(

            LOADED_MODULES

        ),


        "loaded":

        len(

            [

            x for x in LOADED_MODULES.values()

            if x["status"] == "loaded"

            ]

        ),


        "status":

        "active"

    }
