# version_compare.py
# Saeed Core v10.9
# Version Compare Engine


import re
import datetime





COMPARE_LOG = []







def normalize_version(version):


    if not version:


        return [0, 0, 0]



    numbers = re.findall(

        r"\d+",

        version

    )



    result = [

        int(x)

        for x in numbers

    ]





    while len(result) < 3:


        result.append(0)





    return result[:3]









def compare_versions(

    current,

    latest

):


    current_v = normalize_version(

        current

    )


    latest_v = normalize_version(

        latest

    )





    result = {


        "current":

        current,


        "latest":

        latest,


        "upgrade_needed":

        False,


        "time":

        str(datetime.datetime.now())

    }






    if latest_v > current_v:


        result["upgrade_needed"] = True


        result["status"] = "new_version_found"





    elif latest_v == current_v:


        result["status"] = "already_updated"





    else:


        result["status"] = "current_is_newer"







    COMPARE_LOG.append(

        result

    )



    return result









def needs_upgrade(

    current,

    latest

):


    result = compare_versions(

        current,

        latest

    )


    return result["upgrade_needed"]









def compare_status():


    return {


        "comparisons":

        len(

            COMPARE_LOG

        ),


        "status":

        "active"

  }
