# auto_upgrade_agent.py
# Saeed Core v11.2
# Auto Upgrade Agent Core


import datetime





from version_compare import (
    needs_upgrade
)


from github_update_source import (
    get_latest_version
)


from update_downloader import (
    download_file
)


from upgrade_self_test import (
    run_self_test
)


from upgrade_installer import (
    install_package
)


from upgrade_learning import (
    learn_from_upgrade
)








AGENT_LOG = []









def run_auto_upgrade(

    owner,

    repo,

    current_version,

    update_files

):


    result = {


        "time":

        str(datetime.datetime.now()),


        "status":

        "started"

    }








    # دریافت آخرین نسخه

    latest = get_latest_version(

        owner,

        repo

    )






    if not latest:


        result["status"] = "no_version"


        return result







    # مقایسه نسخه‌ها


    if not needs_upgrade(

        current_version,

        latest

    ):


        result["status"] = "already_updated"


        return result







    # تست سلامت قبل از ارتقا


    test = run_self_test()



    if not test["success"]:


        result["status"] = "blocked"


        result["reason"] = "self test failed"


        return result







    # نصب فایل‌ها


    install_result = install_package(

        update_files

    )





    result["install"] = install_result







    if install_result["status"] == "completed":


        result["status"] = "success"


        learn_from_upgrade(

            latest,

            "success"

        )






    else:


        result["status"] = "failed"


        learn_from_upgrade(

            latest,

            "failed",

            [

                "install_error"

            ]

        )








    AGENT_LOG.append(

        result

    )



    return result









def agent_status():


    return {


        "runs":

        len(

            AGENT_LOG

        ),


        "status":

        "active"

        }
