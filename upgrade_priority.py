# upgrade_priority.py
# Saeed Core v10.2
# Upgrade Priority System


import datetime





PRIORITY_LOG = []








HIGH_PRIORITY_FILES = [

    "main.py",

    "config.py",

    "database.py",

    "security.py"

]








def calculate_priority(file_name):


    result = {


        "file":

        file_name,


        "priority":

        "low",


        "time":

        str(datetime.datetime.now())

    }







    if file_name in HIGH_PRIORITY_FILES:


        result["priority"] = "high"






    elif file_name.endswith(

        ".json"

    ):


        result["priority"] = "medium"







    PRIORITY_LOG.append(

        result

    )



    return result







def analyze_files_priority(files):


    results = []



    for file in files:


        results.append(

            calculate_priority(

                file

            )

        )



    return sorted(

        results,

        key=lambda x:

        {

            "high": 1,

            "medium": 2,

            "low": 3

        }.get(

            x["priority"],

            3

        )

    )









def priority_status():


    return {


        "analyzed":

        len(

            PRIORITY_LOG

        ),


        "status":

        "active"

    }
