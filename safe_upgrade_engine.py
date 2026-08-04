# safe_upgrade_engine.py
# Saeed Core v9.8
# Safe Automatic Upgrade Engine


import datetime



from upgrade_self_test import (
    run_self_test
)


from final_auto_upgrade_engine import (
    run_full_upgrade
)


from upgrade_reporter import (
    create_report,
    save_report
)


from version_manager import (
    current_version
)







SAFE_LOG = []








def run_safe_upgrade():


    old_version = current_version()



    result = {


        "time":

        str(datetime.datetime.now()),


        "status":

        "started"

    }






    # اجرای تست سلامت

    test_result = run_self_test()



    result["self_test"] = test_result






    if not test_result["success"]:


        result["status"] = "blocked"


        result["reason"] = "self test failed"



        SAFE_LOG.append(

            result

        )


        return result







    # اجرای ارتقای اصلی


    upgrade_result = run_full_upgrade()



    result["upgrade"] = upgrade_result


    result["status"] = "completed"







    report = create_report(

        old_version,


        upgrade_result.get(

            "new_version",

            old_version

        ),


        upgrade_result.get(

            "results",

            []

        ),


        result["status"]

    )



    save_report(

        report

    )






    SAFE_LOG.append(

        result

    )



    return result









def safe_upgrade_status():


    return {


        "runs":

        len(

            SAFE_LOG

        ),


        "status":

        "active"

    }
