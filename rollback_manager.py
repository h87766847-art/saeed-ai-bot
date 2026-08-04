# rollback_manager.py
# Saeed Core v8.7
# Safe Upgrade Rollback System


import os
import shutil
import json
import datetime





ROLLBACK_LOG = "rollback_log.json"






def load_logs():


    if not os.path.exists(

        ROLLBACK_LOG

    ):


        return []



    with open(

        ROLLBACK_LOG,

        "r",

        encoding="utf-8"

    ) as file:


        return json.load(file)









def save_logs(data):


    with open(

        ROLLBACK_LOG,

        "w",

        encoding="utf-8"

    ) as file:


        json.dump(

            data,

            file,

            ensure_ascii=False,

            indent=4

        )









def create_backup(

    file_path

):


    if not os.path.exists(

        file_path

    ):


        return None





    backup_path = (

        file_path

        +

        ".rollback_backup"

    )



    shutil.copy2(

        file_path,

        backup_path

    )



    return backup_path









def rollback_file(

    file_path,

    backup_path

):


    result = {


        "file":

        file_path,


        "status":

        "failed",


        "time":

        str(datetime.datetime.now())

    }







    try:


        if os.path.exists(

            backup_path

        ):


            shutil.copy2(

                backup_path,

                file_path

            )


            result["status"] = "restored"





        else:


            result["error"] = "backup not found"






    except Exception as e:


        result["error"] = str(e)








    logs = load_logs()


    logs.append(

        result

    )


    save_logs(

        logs

    )



    return result







def rollback_status():


    return {


        "rollback_logs":

        len(

            load_logs()

        ),


        "status":

        "active"

    }
