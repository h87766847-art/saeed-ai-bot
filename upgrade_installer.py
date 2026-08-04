# upgrade_installer.py
# Saeed Core v10.6
# Upgrade Installer Engine


import os
import shutil
import datetime





INSTALL_LOG = []







def create_backup(file_path):


    if not os.path.exists(file_path):

        return None



    backup = file_path + ".backup"



    shutil.copy2(

        file_path,

        backup

    )



    return backup







def install_file(

    old_path,

    new_path

):


    result = {


        "file":

        old_path,


        "status":

        "failed",


        "time":

        str(datetime.datetime.now())

    }





    try:


        # ساخت پوشه مقصد اگر نبود

        folder = os.path.dirname(

            old_path

        )



        if folder and not os.path.exists(folder):


            os.makedirs(folder)






        # بکاپ فایل قدیمی

        backup = create_backup(

            old_path

        )



        result["backup"] = backup







        # جایگزینی فایل جدید

        shutil.copy2(

            new_path,

            old_path

        )





        result["status"] = "installed"






    except Exception as e:


        result["error"] = str(e)







    INSTALL_LOG.append(

        result

    )



    return result







def install_package(

    files

):


    results = []



    for item in files:


        result = install_file(

            item["old"],

            item["new"]

        )


        results.append(

            result

        )



    return {


        "status":

        "completed",


        "results":

        results

    }









def installer_status():


    return {


        "installed":

        len(

            INSTALL_LOG

        ),


        "status":

        "active"

    }
