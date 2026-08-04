# backup_engine.py
# Saeed Core v7.5
# Automatic Backup System


import os
import shutil
import datetime





BACKUP_FOLDER = "saeed_backups"







def create_backup(filename):


    if not os.path.exists(BACKUP_FOLDER):

        os.makedirs(BACKUP_FOLDER)





    if not os.path.exists(filename):

        return {

            "status": "error",

            "message": "file not found"

        }







    name = os.path.basename(filename)



    timestamp = datetime.datetime.now().strftime(

        "%Y%m%d_%H%M%S"

    )



    backup_name = (

        name +

        "_" +

        timestamp

        +

        ".backup"

    )



    destination = os.path.join(

        BACKUP_FOLDER,

        backup_name

    )



    shutil.copy2(

        filename,

        destination

    )



    return {

        "status":

        "success",


        "backup":

        destination

    }









def list_backups():


    if not os.path.exists(BACKUP_FOLDER):

        return []



    return os.listdir(

        BACKUP_FOLDER

    )









def restore_backup(

        backup_file,

        target_file

):


    if not os.path.exists(

        backup_file

    ):


        return False



    shutil.copy2(

        backup_file,

        target_file

    )


    return True







def backup_status():


    return {


        "folder":

        BACKUP_FOLDER,


        "backups":

        len(

            list_backups()

        ),


        "status":

        "active"

    }
