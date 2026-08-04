# self_upgrade_engine.py
# Saeed Core
# Advanced Self Upgrade Management System


import os
import shutil
import datetime
import json





VERSION_FILE = "saeed_version.json"

BACKUP_FOLDER = "saeed_backups"

UPGRADE_LOG = "upgrade_history.json"







def load_version():


    if not os.path.exists(VERSION_FILE):


        return {


            "version":

            "6.3",


            "build":

            1

        }





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

            ensure_ascii=False,

            indent=4

        )







def create_backup(filename):


    if not os.path.exists(

        BACKUP_FOLDER

    ):


        os.makedirs(

            BACKUP_FOLDER

        )




    if os.path.exists(filename):


        backup_name = (

            BACKUP_FOLDER +

            "/" +

            filename +

            "_" +

            datetime.datetime.now().strftime(

                "%Y%m%d_%H%M%S"

            )

        )


        shutil.copy(

            filename,

            backup_name

        )


        return backup_name





    return None







def test_file(filename):


    try:


        with open(

            filename,

            "r",

            encoding="utf-8"

        ) as file:


            code = file.read()



        compile(

            code,

            filename,

            "exec"

        )



        return True



    except Exception:


        return False







def upgrade_module(filename):


    backup = create_backup(

        filename

    )



    success = test_file(

        filename

    )



    log = {


        "file":

        filename,


        "backup":

        backup,


        "success":

        success,


        "time":

        str(

            datetime.datetime.now()

        )

    }



    save_upgrade_log(

        log

    )



    return log







def save_upgrade_log(data):


    logs = []



    if os.path.exists(

        UPGRADE_LOG

    ):


        with open(

            UPGRADE_LOG,

            "r",

            encoding="utf-8"

        ) as file:


            logs = json.load(

                file

            )



    logs.append(

        data

    )



    with open(

        UPGRADE_LOG,

        "w",

        encoding="utf-8"

    ) as file:


        json.dump(

            logs,

            file,

            ensure_ascii=False,

            indent=4

        )







def upgrade_status():


    return {


        "version":

        load_version(),


        "system":

        "ready",


        "time":

        str(

            datetime.datetime.now()

        )

  }
