# upgrade_validator.py
# Saeed Core v7.8
# Upgrade Validation System


import os
import datetime





VALIDATION_LOG = []








def validate_file_item(item):


    result = {


        "file":

        item.get(

            "name"

        ),


        "valid":

        False,


        "errors":

        [],


        "time":

        str(datetime.datetime.now())

    }






    filename = item.get(

        "name"

    )



    action = item.get(

        "action"

    )







    if not filename:


        result["errors"].append(

            "File name missing"

        )




    if action not in [

        "install",

        "replace"

    ]:


        result["errors"].append(

            "Invalid action"

        )






    if filename:


        result["valid"] = True





    if len(result["errors"]) == 0:


        result["valid"] = True





    VALIDATION_LOG.append(

        result

    )



    return result







def validate_package(package):


    result = {


        "version":

        package.get(

            "version"

        ),


        "valid":

        True,


        "files":

        []

    }







    for item in package.get(

        "files",

        []

    ):


        check = validate_file_item(

            item

        )



        result["files"].append(

            check

        )



        if not check["valid"]:


            result["valid"] = False







    return result









def get_validation_log():


    return VALIDATION_LOG









def validator_status():


    return {


        "checks":

        len(

            VALIDATION_LOG

        ),


        "status":

        "active"

    }
