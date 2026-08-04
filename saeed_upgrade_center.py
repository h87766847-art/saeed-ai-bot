# saeed_upgrade_center.py
# Saeed Core v7.6
# Automatic Upgrade Center
#
# مسئول:
# - بررسی بسته ارتقا
# - بکاپ
# - جایگزینی فایل‌های قدیمی
# - نصب فایل‌های جدید
# - ثبت گزارش


import os
import json
import shutil
import datetime





from upgrade_manager import (
    prepare_upgrade,
    register_upgrade
)


from version_manager import (
    current_version,
    add_update
)


from module_loader import (
    load_module
)





UPGRADE_LOG_FILE = "saeed_upgrade_log.json"






def load_logs():


    if not os.path.exists(

        UPGRADE_LOG_FILE

    ):


        return []



    with open(

        UPGRADE_LOG_FILE,

        "r",

        encoding="utf-8"

    ) as file:


        return json.load(file)







def save_logs(data):


    with open(

        UPGRADE_LOG_FILE,

        "w",

        encoding="utf-8"

    ) as file:


        json.dump(

            data,

            file,

            ensure_ascii=False,

            indent=4

        )









def backup_file(filename):


    if not os.path.exists(filename):

        return None



    backup_name = (

        filename

        +

        ".backup_"

        +

        datetime.datetime.now()

        .strftime("%Y%m%d_%H%M%S")

    )



    shutil.copy2(

        filename,

        backup_name

    )



    return backup_name









def install_new_file(

    filename,

    content

):


    with open(

        filename,

        "w",

        encoding="utf-8"

    ) as file:


        file.write(

            content

        )



    return True









def upgrade_file(

    filename,

    content,

    description=""

):


    result = {


        "file": filename,


        "status": "unknown",


        "time":

        str(datetime.datetime.now())

    }





    try:


        if os.path.exists(filename):


            backup_file(

                filename

            )



            prepare_upgrade(

                filename

            )






        install_new_file(

            filename,

            content

        )





        register_upgrade(

            filename,

            description

        )





        result["status"] = "updated"





    except Exception as e:


        result["status"] = "failed"

        result["error"] = str(e)






    logs = load_logs()


    logs.append(

        result

    )


    save_logs(

        logs

    )



    return result







def install_module(

    filename

):


    name = filename.replace(

        ".py",

        ""

    )



    try:


        result = load_module(

            name

        )


        return {


            "module":

            name,


            "loaded":

            result

        }



    except Exception as e:


        return {


            "module":

            name,


            "error":

            str(e)

        }









def upgrade_package(

    package

):


    results = []



    files = package.get(

        "files",

        []

    )




    for item in files:


        result = upgrade_file(

            item["name"],

            item["content"],

            item.get(

                "description",

                ""

            )

        )



        results.append(

            result

        )



        if item["name"].endswith(

            ".py"

        ):


            install_module(

                item["name"]

            )







    add_update(

        "Automatic upgrade completed"

    )



    return {


        "version":

        current_version(),


        "results":

        results,


        "status":

        "completed"

    }







def upgrade_status():


    return {


        "system":

        "Saeed Upgrade Center",


        "version":

        current_version(),


        "logs":

        len(

            load_logs()

        )

    }
