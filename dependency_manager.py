# dependency_manager.py
# Saeed Core v7.6
# Dependency Management System


import importlib
import datetime





DEPENDENCIES = {

    "core": [

        "brain",

        "core_router",

        "memory_manager"

    ],


    "intelligence": [

        "context_intelligence",

        "planner_intelligence",

        "decision_intelligence"

    ],


    "system": [

        "backup_engine",

        "self_upgrade_engine",

        "system_logger",

        "version_manager"

    ]

}







RESULTS = {}







def check_dependency(module):


    try:


        importlib.import_module(

            module

        )


        return {


            "module":

            module,


            "status":

            "OK"

        }



    except Exception as e:


        return {


            "module":

            module,


            "status":

            "ERROR",


            "error":

            str(e)

        }









def scan_dependencies():


    global RESULTS



    RESULTS = {


        "time":

        str(

            datetime.datetime.now()

        ),


        "modules":

        []

    }



    for group in DEPENDENCIES.values():


        for module in group:


            RESULTS["modules"].append(

                check_dependency(module)

            )



    return RESULTS







def missing_dependencies():


    scan = scan_dependencies()



    return [

        item["module"]

        for item in scan["modules"]

        if item["status"] == "ERROR"

    ]









def dependency_status():


    missing = missing_dependencies()



    return {


        "total":

        sum(

            len(x)

            for x in DEPENDENCIES.values()

        ),


        "missing":

        len(missing),


        "status":

        "healthy"

        if len(missing) == 0

        else "warning"

    }
