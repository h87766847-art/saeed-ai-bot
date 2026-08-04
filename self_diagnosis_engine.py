# self_diagnosis_engine.py
# Saeed Core
# Advanced Self Diagnosis System


import os
import datetime
import importlib.util





MODULES = [

    "brain.py",

    "core_router.py",

    "memory_manager.py",

    "context_intelligence.py",

    "decision_intelligence.py",

    "planner_intelligence.py"

]







def check_file(

        filename

):


    result = {


        "file":

        filename,


        "exists":

        False,


        "valid":

        False

    }





    if os.path.exists(

        filename

    ):


        result["exists"] = True



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



            result["valid"] = True



        except Exception as e:


            result["error"] = str(e)





    return result







def diagnose_system():


    report = []



    for module in MODULES:


        report.append(

            check_file(

                module

            )

        )



    healthy = 0



    for item in report:


        if item["valid"]:


            healthy += 1





    return {


        "total_modules":

        len(MODULES),


        "healthy":

        healthy,


        "issues":

        len(MODULES) - healthy,


        "details":

        report,


        "time":

        str(

            datetime.datetime.now()

        )

    }







def check_import(

        module_name

):


    try:


        spec = importlib.util.find_spec(

            module_name

        )



        return spec is not None



    except Exception:


        return False







def diagnosis_status():


    report = diagnose_system()



    return {


        "status":

        "healthy"

        if report["issues"] == 0

        else "warning",


        "report":

        report

    }
