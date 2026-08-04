# system_test.py
# Saeed Core v7.5
# Full System Diagnostic Test


import datetime
import importlib





MODULES = [

    "main",

    "brain",

    "core_router",

    "memory_manager",

    "context_intelligence",

    "planner_intelligence",

    "decision_intelligence",

    "core_manager",

    "capability_manager",

    "plugin_manager",

    "module_loader",

    "event_engine",

    "learning_engine",

    "api_bridge",

    "sandbox_engine",

    "security_guard"

]







RESULTS = {}







def test_module(

        module_name

):


    try:


        importlib.import_module(

            module_name

        )


        RESULTS[module_name] = {


            "status":

            "OK"

        }



    except Exception as e:


        RESULTS[module_name] = {


            "status":

            "ERROR",


            "error":

            str(e)

        }








def run_test():


    for module in MODULES:


        test_module(

            module

        )



    return RESULTS







def report():


    result = run_test()



    print(

        "\n=== Saeed Core Test ==="

    )


    print(

        "Time:",

        datetime.datetime.now()

    )



    for name, data in result.items():


        print(

            name,

            ":",

            data

        )



    print(

        "======================"

    )








if __name__ == "__main__":


    report()
