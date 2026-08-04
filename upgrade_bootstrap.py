# upgrade_bootstrap.py
# Saeed Core v8.2
# Upgrade Bootstrap System


import datetime





from auto_upgrade_agent import (
    check_upgrade_status
)







BOOT_LOG = []








def log_boot(

    status

):


    BOOT_LOG.append(

        {

            "status":

            status,


            "time":

            str(datetime.datetime.now())

        }

    )









def initialize_upgrade_system():


    try:


        result = check_upgrade_status()



        log_boot(

            result

        )



        return {


            "status":

            "ready",


            "upgrade":

            result

        }






    except Exception as e:



        error = {


            "status":

            "error",


            "message":

            str(e)

        }




        log_boot(

            error

        )



        return error









def get_boot_status():


    return {


        "checks":

        len(

            BOOT_LOG

        ),


        "status":

        "active"

    }
