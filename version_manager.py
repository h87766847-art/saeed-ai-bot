# version_manager.py
# Saeed Core v7.6
# Version Management System


import datetime
import json
import os





VERSION_FILE = "saeed_version.json"







DEFAULT_VERSION = {

    "name": "Saeed Core",

    "version": "7.6",

    "updates": []

}








def load_version():


    if not os.path.exists(VERSION_FILE):

        save_version(

            DEFAULT_VERSION

        )



    with open(

        VERSION_FILE,

        "r",

        encoding="utf-8"

    ) as file:


        return json.load(file)









def save_version(data):


    with open(

        VERSION_FILE,

        "w",

        encoding="utf-8"

    ) as file:


        json.dump(

            data,

            file,

            indent=4,

            ensure_ascii=False

        )








def add_update(

        description

):


    data = load_version()



    data["updates"].append({


        "description":

        description,


        "time":

        str(

            datetime.datetime.now()

        )

    })



    save_version(

        data

    )



    return data







def current_version():


    return load_version()







def version_status():


    data = load_version()



    return {


        "version":

        data["version"],


        "updates":

        len(

            data["updates"]

        ),


        "status":

        "active"

    }
