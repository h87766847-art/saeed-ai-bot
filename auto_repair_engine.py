# auto_repair_engine.py
# Saeed Core
# Advanced Auto Repair System


import os
import datetime
import shutil





REPAIR_LOG = []







def backup_before_repair(

        filename

):


    if not os.path.exists(

        filename

    ):


        return False





    backup = (

        filename

        +

        ".repair_backup_"

        +

        datetime.datetime.now().strftime(

            "%Y%m%d_%H%M%S"

        )

    )



    shutil.copy(

        filename,

        backup

    )



    return backup







def check_python_file(

        filename

):


    try:


        with open(

            filename,

            "r",

            encoding="utf-8"

        ) as file:


            code = file.read()



        compile(

            code,

            filename,

            "exec"

        )



        return {


            "healthy":

            True,


            "error":

            None

        }





    except Exception as e:


        return {


            "healthy":

            False,


            "error":

            str(e)

        }









def repair_check(

        filename

):


    result = check_python_file(

        filename

    )



    log = {


        "file":

        filename,


        "before":

        result,


        "time":

        str(

            datetime.datetime.now()

        )

    }





    if not result["healthy"]:


        backup = backup_before_repair(

            filename

        )


        log["backup"] = backup



        log["action"] = (

            "backup_created"

        )



    else:


        log["action"] = (

            "no_repair_needed"

        )





    REPAIR_LOG.append(

        log

    )



    return log







def get_repair_history():


    return REPAIR_LOG








def repair_status():


    return {


        "repairs":

        len(REPAIR_LOG),


        "status":

        "ready"

    }
