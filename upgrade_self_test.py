# upgrade_self_test.py
# Saeed Core v9.7
# Upgrade Self Test System


import os
import datetime
import importlib





TEST_LOG = []







def test_file_exists(filename):


    result = {


        "test":

        "file_exists",


        "file":

        filename,


        "status":

        False

    }





    if os.path.exists(filename):


        result["status"] = True





    return result









def test_module_import(module_name):


    result = {


        "test":

        "module_import",


        "module":

        module_name,


        "status":

        False

    }







    try:


        importlib.import_module(

            module_name

        )


        result["status"] = True





    except Exception as e:


        result["error"] = str(e)







    return result









def run_self_test():


    results = []




    required_files = [


        "saeed_upgrade_center.py",


        "upgrade_pipeline.py",


        "upgrade_validator.py",


        "final_auto_upgrade_engine.py"

    ]







    for file in required_files:


        results.append(

            test_file_exists(

                file

            )

        )








    required_modules = [


        "saeed_upgrade_center",


        "upgrade_pipeline",


        "upgrade_validator"

    ]







    for module in required_modules:


        results.append(

            test_module_import(

                module

            )

        )








    success = all(

        item["status"]

        for item in results

    )







    report = {


        "time":

        str(datetime.datetime.now()),


        "success":

        success,


        "results":

        results

    }






    TEST_LOG.append(

        report

    )



    return report









def self_test_status():


    return {


        "tests":

        len(

            TEST_LOG

        ),


        "status":

        "active"

    }
