# module_loader.py
# Saeed Core v7.5
# Automatic Module Loader


import os
import importlib
import datetime





LOADED_MODULES = {}





IGNORE_FILES = [

    "__init__.py",

    "module_loader.py"

]








def discover_modules(

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


                modules.append(

                    file[:-3]

                )



    return modules







def load_module(

        name

):


    try:


        module = importlib.import_module(

            name

        )



        LOADED_MODULES[name] = {


            "module":

            module,


            "status":

            "loaded",


            "time":

            str(

                datetime.datetime.now()

            )

        }



        return True




    except Exception as e:



        LOADED_MODULES[name] = {


            "status":

            "failed",


            "error":

            str(e)

        }



        return False







def load_all_modules(

        folder="."

):


    results = {}



    for module in discover_modules(

        folder

    ):


        results[module] = load_module(

            module

        )



    return results







def reload_module(

        name

):


    if name not in LOADED_MODULES:


        return False



    try:


        importlib.reload(

            LOADED_MODULES[name]["module"]

        )


        return True



    except Exception:


        return False







def get_loaded_modules():


    return LOADED_MODULES







def loader_status():


    return {


        "total":

        len(

            LOADED_MODULES

        ),


        "loaded":

        len(

            [

            x for x in LOADED_MODULES.values()

            if x.get("status") == "loaded"

            ]

        ),


        "status":

        "active"

}
