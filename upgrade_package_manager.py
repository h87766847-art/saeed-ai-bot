# upgrade_package_manager.py
# Saeed Core v7.7
# Upgrade Package Reader


import os
import json
import datetime





PACKAGE_LOG = "upgrade_packages.json"






def load_package_log():


    if not os.path.exists(PACKAGE_LOG):

        return []



    with open(

        PACKAGE_LOG,

        "r",

        encoding="utf-8"

    ) as file:


        return json.load(file)








def save_package_log(data):


    with open(

        PACKAGE_LOG,

        "w",

        encoding="utf-8"

    ) as file:


        json.dump(

            data,

            file,

            ensure_ascii=False,

            indent=4

        )









def read_manifest(

    path="manifest.json"

):


    if not os.path.exists(path):

        return None




    with open(

        path,

        "r",

        encoding="utf-8"

    ) as file:


        return json.load(file)









def analyze_package(

    manifest

):


    result = {


        "version":

        manifest.get(

            "version",

            "unknown"

        ),


        "files":

        [],


        "time":

        str(datetime.datetime.now())

    }






    for item in manifest.get(

        "files",

        []

    ):


        result["files"].append(

            {


                "name":

                item.get(

                    "name"

                ),


                "action":

                item.get(

                    "action",

                    "replace"

                )


            }

        )




    return result







def register_package(

    package

):


    data = load_package_log()



    data.append(

        package

    )



    save_package_log(

        data

    )



    return package







def package_status():


    return {


        "packages":

        len(

            load_package_log()

        ),


        "status":

        "active"

    }
