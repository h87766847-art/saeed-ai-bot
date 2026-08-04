# upgrade_intelligence.py
# Saeed Core v10.0
# Upgrade Intelligence Layer


import datetime





INTELLIGENCE_LOG = []








def analyze_upgrade(

    current_version,

    new_version,

    changed_files

):


    result = {


        "time":

        str(datetime.datetime.now()),


        "current_version":

        current_version,


        "new_version":

        new_version,


        "files_changed":

        len(

            changed_files

        ),


        "decision":

        None,


        "risk":

        None

    }







    files_count = len(

        changed_files

    )






    if files_count == 0:


        result["decision"] = "skip"

        result["risk"] = "none"






    elif files_count <= 3:


        result["decision"] = "partial_upgrade"

        result["risk"] = "low"







    elif files_count <= 10:


        result["decision"] = "normal_upgrade"

        result["risk"] = "medium"








    else:


        result["decision"] = "full_upgrade"

        result["risk"] = "high"







    INTELLIGENCE_LOG.append(

        result

    )



    return result









def should_upgrade(

    analysis

):


    if analysis.get(

        "decision"

    ) == "skip":


        return False





    return True









def intelligence_status():


    return {


        "decisions":

        len(

            INTELLIGENCE_LOG

        ),


        "status":

        "active"

    }
