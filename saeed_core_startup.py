# saeed_core_startup.py
# Saeed Core v9.1
# Startup Integration


import datetime





from final_auto_upgrade_engine import (
    run_full_upgrade,
    engine_status
)





STARTUP_LOG = []







def initialize_saeed_core():


    result = {


        "time":

        str(datetime.datetime.now()),


        "upgrade":

        None

    }




    try:


        upgrade_result = run_full_upgrade()



        result["upgrade"] = upgrade_result





        result["status"] = "ready"






    except Exception as e:


        result["status"] = "running_without_upgrade"


        result["error"] = str(e)








    STARTUP_LOG.append(

        result

    )



    return result









def saeed_status():


    return {


        "startup_checks":

        len(

            STARTUP_LOG

        ),


        "upgrade_engine":

        engine_status()

    }
