# update_server.py
# Saeed Core v8.0
# Update Source Manager


import os
import json
import datetime





SERVER_FILE = "updates/update_index.json"







def load_update_index():


    if not os.path.exists(

        SERVER_FILE

    ):


        return {

            "versions": []

        }




    with open(

        SERVER_FILE,

        "r",

        encoding="utf-8"

    ) as file:


        return json.load(file)









def get_available_updates():


    data = load_update_index()



    return data.get(

        "versions",

        []

    )









def check_new_version(

    current_version

):


    updates = get_available_updates()



    available = []



    for item in updates:


        if item.get(

            "version"

        ) > current_version:


            available.append(

                item

            )





    return available









def get_latest_update():


    updates = get_available_updates()



    if not updates:


        return None





    return sorted(

        updates,

        key=lambda x: x.get(

            "version",

            "0"

        ),

        reverse=True

    )[0]









def create_update_record(

    version,

    description

):


    return {


        "version":

        version,


        "description":

        description,


        "created":

        str(datetime.datetime.now())


    }









def server_status():


    return {


        "source":

        "active",


        "updates":

        len(

            get_available_updates()

        )

          }
