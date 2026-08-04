# github_update_source.py
# Saeed Core v10.8
# GitHub Update Source Connector


import json
import urllib.request
import datetime





GITHUB_LOG = []








def get_github_json(url):


    result = {


        "url":

        url,


        "status":

        "failed",


        "time":

        str(datetime.datetime.now())

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


        result["data"] = data





    except Exception as e:


        result["error"] = str(e)






    GITHUB_LOG.append(

        result

    )



    return result









def check_latest_release(

    owner,

    repo

):


    url = (

        "https://api.github.com/repos/"

        + owner

        + "/"

        + repo

        + "/releases/latest"

    )



    return get_github_json(

        url

    )









def get_latest_version(

    owner,

    repo

):


    release = check_latest_release(

        owner,

        repo

    )




    if release.get(

        "status"

    ) != "success":


        return None





    return release["data"].get(

        "tag_name"

    )









def github_status():


    return {


        "requests":

        len(

            GITHUB_LOG

        ),


        "status":

        "active"

    }
