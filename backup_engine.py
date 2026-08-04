# backup_engine.py
# Saeed Core
# Advanced Backup Management System


import os
import shutil
import datetime
import json





BACKUP_DIR = "saeed_backup"

BACKUP_HISTORY = "backup_history.json"







def create_backup_folder():


    if not os.path.exists(

        BACKUP_DIR

    ):


        os.makedirs(

            BACKUP_DIR

        )







def backup_file(

        filename

):


    create_backup_folder()



    if not os.path.exists(

        filename

    ):


        return False





    timestamp = datetime.datetime.now().strftime(

        "%Y%m%d_%H%M%S"

    )



    destination = (

        BACKUP_DIR

        +

        "/"

        +

        filename.replace(

            "/",

            "_"

        )

        +

        "_"

        +

        timestamp

    )



    shutil.copy(

        filename,

        destination

    )



    save_history(

        {

        "file":

        filename,


        "backup":

        destination,


        "time":

        str(

            datetime.datetime.now()

        )

        }

    )



    return destination








def backup_project(

        files

):


    results = []



    for file in files:


        result = backup_file(

            file

        )



        results.append(

            result

        )



    return results







def save_history(

        data

):


    history = []



    if os.path.exists(

        BACKUP_HISTORY

    ):


        with open(

            BACKUP_HISTORY,

            "r",

            encoding="utf-8"

        ) as file:


            history = json.load(

                file

            )




    history.append(

        data

    )



    with open(

        BACKUP_HISTORY,

        "w",

        encoding="utf-8"

    ) as file:


        json.dump(

            history,

            file,

            ensure_ascii=False,

            indent=4

        )








def get_backup_history():


    if not os.path.exists(

        BACKUP_HISTORY

    ):


        return []



    with open(

        BACKUP_HISTORY,

        "r",

        encoding="utf-8"

    ) as file:


        return json.load(

            file

        )








def backup_status():


    return {


        "folder":

        BACKUP_DIR,


        "backups":

        len(

            get_backup_history()

        ),


        "status":

        "active"

    }
