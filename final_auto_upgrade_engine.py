# final_auto_upgrade_engine.py
# Saeed Core v9.0
# Final Automatic Upgrade Engine


import datetime





from auto_upgrade_agent import (
    check_upgrade_status
)


from update_server import (
    get_latest_update
)


from update_package_builder import (
    package_info
)


from upgrade_security import (
    verify_package
)


from upgrade_validator import (
    validate_package
)


from upgrade_pipeline import (
    run_upgrade
)


from upgrade_reporter import (
    create_report,
    save_report
)


from version_manager import (
    current_version
)








ENGINE_LOG = []







def run_full_upgrade():


    old_version = current_version()





    status = check_upgrade_status()





    if not status.get(

        "upgrade_needed",

        False

    ):


        return {


            "status":

            "no_update",


            "version":

            old_version

        }








    update = get_latest_update()





    if not update:


        return {


            "status":

            "failed",


            "error":

            "update not found"

        }









    manifest = update.get(

        "manifest"

    )






    security = verify_package(

        manifest

    )





    if not security["valid"]:


        return {


            "status":

            "blocked",


            "reason":

            "security check failed"

        }








    validation = validate_package(

        manifest

    )







    if not validation["valid"]:


        return {


            "status":

            "blocked",


            "reason":

            "validation failed"

        }









    result = run_upgrade(

        manifest

    )







    report = create_report(

        old_version,


        update.get(

            "version"

        ),


        result.get(

            "results",

            []

        ),


        result.get(

            "status"

        )

    )





    save_report(

        report

    )







    ENGINE_LOG.append(

        report

    )







    return report









def engine_status():


    return {


        "engine":

        "Saeed Core v9.0",


        "runs":

        len(

            ENGINE_LOG

        ),


        "status":

        "active"

      }
