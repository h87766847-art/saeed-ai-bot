# upgrade_manager.py
# Saeed Core v7.6
# Automatic Upgrade Manager


import datetime





try:
    from backup_engine import create_backup

except Exception:
    create_backup = None





try:
    from version_manager import add_update

except Exception:
    add_update = None





UPGRADE_HISTORY = []







def prepare_upgrade(filename):


    result = {


        "file":

        filename,


        "time":

        str(datetime.datetime.now()),


        "backup":

        None,


        "status":

        "prepared"

    }



    if create_backup:


        try:

            result["backup"] = create_backup(

                filename

            )


        except Exception:

            pass



    return result







def register_upgrade(

        filename,

        description

):


    upgrade = {


        "file":

        filename,


        "description":

        description,


        "time":

        str(datetime.datetime.now()),


        "status":

        "completed"

    }



    UPGRADE_HISTORY.append(

        upgrade

    )



    if add_update:


        try:

            add_update(

                description

            )


        except Exception:

            pass



    return upgrade







def get_upgrade_history():


    return UPGRADE_HISTORY







def upgrade_manager_status():


    return {


        "upgrades":

        len(UPGRADE_HISTORY),


        "status":

        "active"

    }
