# file_monitor.py
# Saeed Core v7.6
# File Health Monitoring System


import os
import datetime





CORE_FILES = [

    "main.py",

    "brain.py",

    "core_router.py",

    "memory_manager.py",

    "context_intelligence.py",

    "planner_intelligence.py",

    "decision_intelligence.py",

    "backup_engine.py",

    "self_upgrade_engine.py",

    "system_logger.py",

    "version_manager.py"

]







REPORT = {}







def check_file(filename):


    if os.path.exists(filename):


        return {


            "file":

            filename,


            "status":

            "OK"

        }



    return {


        "file":

        filename,


        "status":

        "MISSING"

    }









def scan_system():


    global REPORT


    REPORT = {



        "time":

        str(

            datetime.datetime.now()

        ),


        "files":

        []

    }



    for file in CORE_FILES:


        REPORT["files"].append(

            check_file(file)

        )



    return REPORT







def missing_files():


    result = scan_system()



    return [

        item["file"]

        for item in result["files"]

        if item["status"] == "MISSING"

    ]









def monitor_status():


    missing = missing_files()



    return {


        "total":

        len(CORE_FILES),


        "missing":

        len(missing),


        "status":

        "healthy"

        if len(missing) == 0

        else "warning"

    }
