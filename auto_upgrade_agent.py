# auto_upgrade_agent.py
# Saeed Core v8.1
# Automatic Upgrade Agent


import datetime





from version_manager import (
    current_version
)


from update_server import (
    check_new_version,
    get_latest_update
)


from upgrade_pipeline import (
    run_upgrade
)







AUTO_LOG = []








def log_action(

    action,

    data

):


    AUTO_LOG.append(

        {

            "action":

            action,


            "data":

            data,


            "time":

            str(datetime.datetime.now())

        }

    )









def check_upgrade_status():


    version = current_version()



    updates = check_new_version(

        version

    )



    result = {


        "current":

        version,


        "available":

        updates,


        "upgrade_needed":

        len(updates) > 0

    }




    log_action(

        "check",

        result

    )



    return result







def start_auto_upgrade():


    status = check_upgrade_status()



    if not status["upgrade_needed"]:


        return {


            "status":

            "no_update",


            "message":

            "نسخه فعلی به‌روز است"

        }







    update = get_latest_update()



    if not update:


        return {


            "status":

            "failed",


            "message":

            "بسته ارتقا پیدا نشد"

        }







    result = run_upgrade(

        update.get(

            "manifest",

            "manifest.json"

        )

    )





    log_action(

        "upgrade",

        result

    )



    return result







def auto_upgrade_status():


    return {


        "runs":

        len(

            AUTO_LOG

        ),


        "status":

        "active"

    }
