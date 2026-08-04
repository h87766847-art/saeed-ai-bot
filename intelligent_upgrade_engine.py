# intelligent_upgrade_engine.py
# Saeed Core v10.1
# Intelligent Upgrade Decision Engine


import datetime





from upgrade_intelligence import (
    analyze_upgrade,
    should_upgrade
)


from safe_upgrade_engine import (
    run_safe_upgrade
)






INTELLIGENT_LOG = []








def run_intelligent_upgrade(

    current_version,

    new_version,

    changed_files

):


    analysis = analyze_upgrade(

        current_version,

        new_version,

        changed_files

    )





    result = {


        "time":

        str(datetime.datetime.now()),


        "analysis":

        analysis

    }







    if not should_upgrade(

        analysis

    ):


        result["status"] = "skipped"


        result["reason"] = "upgrade not required"



        INTELLIGENT_LOG.append(

            result

        )


        return result







    upgrade_result = run_safe_upgrade()





    result["status"] = "executed"


    result["upgrade"] = upgrade_result





    INTELLIGENT_LOG.append(

        result

    )



    return result









def intelligent_status():


    return {


        "decisions":

        len(

            INTELLIGENT_LOG

        ),


        "status":

        "active"

    }
