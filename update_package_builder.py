# update_package_builder.py
# Saeed Core v8.5
# Update Package Builder


import os
import json
import datetime





def create_manifest(

    version,

    description,

    files

):


    manifest = {


        "version":

        version,


        "description":

        description,


        "created":

        str(datetime.datetime.now()),


        "files":

        files

    }



    return manifest









def save_manifest(

    manifest,

    path="manifest.json"

):


    folder = os.path.dirname(

        path

    )



    if folder and not os.path.exists(folder):


        os.makedirs(

            folder

        )





    with open(

        path,

        "w",

        encoding="utf-8"

    ) as file:


        json.dump(

            manifest,

            file,

            ensure_ascii=False,

            indent=4

        )



    return True









def add_file_entry(

    name,

    action="replace",

    description=""

):


    return {


        "name":

        name,


        "action":

        action,


        "description":

        description

    }









def package_info(

    manifest

):


    return {


        "version":

        manifest.get(

            "version"

        ),


        "files":

        len(

            manifest.get(

                "files",

                []

            )

        ),


        "status":

        "ready"

  }
