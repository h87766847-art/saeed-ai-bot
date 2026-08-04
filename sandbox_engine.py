# sandbox_engine.py
# Saeed Core v7.5
# Secure Sandbox Testing System


import datetime
import uuid





TESTS = {}







def create_test(

        name,

        function

):


    test_id = str(

        uuid.uuid4()

    )



    TESTS[test_id] = {


        "id":

        test_id,


        "name":

        name,


        "function":

        function,


        "status":

        "created",


        "time":

        str(

            datetime.datetime.now()

        )

    }



    return TESTS[test_id]









def run_test(

        test_id

):


    test = TESTS.get(

        test_id

    )



    if not test:


        return {


            "status":

            "error",


            "message":

            "test not found"

        }







    try:


        result = test["function"]()



        test["status"] = "passed"


        test["result"] = result




        return {


            "status":

            "passed",


            "result":

            result

        }





    except Exception as e:


        test["status"] = "failed"


        test["error"] = str(e)



        return {


            "status":

            "failed",


            "error":

            str(e)

        }









def test_component(

        name,

        function

):


    test = create_test(

        name,

        function

    )



    return run_test(

        test["id"]

    )









def get_tests():


    return list(

        TESTS.values()

    )








def sandbox_status():


    return {


        "tests":

        len(TESTS),


        "status":

        "ready",


        "time":

        str(

            datetime.datetime.now()

        )

    }
