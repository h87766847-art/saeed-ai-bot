# update_downloader.py
# Saeed Core v10.7
# Update Downloader Engine


import os
import json
import datetime
import urllib.request





DOWNLOAD_LOG = []






UPDATE_FOLDER = "updates"









def create_update_folder():


    if not os.path.exists(

        UPDATE_FOLDER

    ):


        os.makedirs(

            UPDATE_FOLDER

        )








def download_file(

    url,

    filename

):


    create_update_folder()



    path = os.path.join(

        UPDATE_FOLDER,

        filename

    )



    result = {


        "url":

        url,


        "file":

        path,


        "status":

        "failed",


        "time":

        str(datetime.datetime.now())

    }






    try:


        urllib.request.urlretrieve(

            url,

            path

        )



        result["status"] = "downloaded"






    except Exception as e:


        result["error"] = str(e)







    DOWNLOAD_LOG.append(

        result

    )



    return result









def download_manifest(

    url

):


    result = {


        "status":

        "failed"

    }





    try:


        with urllib.request.urlopen(

            url

        ) as response:


            data = json.loads(

                response.read().decode(

                    "utf-8"

                )

            )



        result["status"] = "success"


        result["manifest"] = data





    except Exception as e:


        result["error"] = str(e)






    return result









def downloader_status():


    return {


        "downloads":

        len(

            DOWNLOAD_LOG

        ),


        "status":

        "active"

    }
