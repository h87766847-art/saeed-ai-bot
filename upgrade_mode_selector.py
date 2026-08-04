# upgrade_mode_selector.py
# Saeed Core v10.3
# Partial Upgrade Decision System


import datetime





MODE_LOG = []








def select_upgrade_mode(

    changed_files

):


    count = len(

        changed_files

    )



    result = {


        "time":

        str(datetime.datetime.now()),


        "files_count":

        count,


        "mode":

        None

    }








    if count == 0:


        result["mode"] = "no_upgrade"







    elif count <= 3:


        result["mode"] = "partial"







    elif count <= 10:


        result["mode"] = "normal"







    else:


        result["mode"] = "full"







    MODE_LOG.append(

        result

    )



    return result







def should_install_mode(

    mode

):


    if mode == "no_upgrade":


        return False



    return True









def mode_status():


    return {


        "decisions":

        len(

            MODE_LOG

        ),


        "status":

        "active"

    }
