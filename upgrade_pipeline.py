# upgrade_pipeline.py
# Saeed Core v7.9
# Complete Upgrade Pipeline


import os
import json
import datetime



from upgrade_package_manager import (
    read_manifest,
    analyze_package,
    register_package
)


from upgrade_validator import (
    validate_package
)


from saeed_upgrade_center import (
    upgrade_package
)






PIPELINE_LOG = "upgrade_pipeline_log.json"







def load_pipeline_log():


    if not os.path.exists(PIPELINE_LOG):

        return []



    with open(

        PIPELINE_LOG,

        "r",

        encoding="utf-8"

    ) as file:


        return json.load(file)









def save_pipeline_log(data):


    with open(

        PIPELINE_LOG,

        "w",

        encoding="utf-8"

    ) as file:


        json.dump(

            data,

            file,

            ensure_ascii=False,

            indent=4

        )









def run_upgrade(

    manifest_path="manifest.json"

):


    result = {


        "time":

        str(datetime.datetime.now()),


        "status":

        "started"

    }







    manifest = read_manifest(

        manifest_path

    )





    if not manifest:


        result["status"] = "failed"

        result["error"] = "Manifest not found"

        return result







    package = analyze_package(

        manifest

    )






    validation = validate_package(

        manifest

    )







    if not validation["valid"]:


        result["status"] = "failed"

        result["error"] = "Validation failed"

        result["validation"] = validation

        return result







    register_package(

        package

    )







    result["upgrade"] = upgrade_package(

        manifest

    )



    result["status"] = "completed"







    logs = load_pipeline_log()


    logs.append(

        result

    )


    save_pipeline_log(

        logs

    )





    return result









def pipeline_status():


    return {


        "runs":

        len(

            load_pipeline_log()

        ),


        "status":

        "active"

  }
