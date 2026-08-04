# main.py
# Saeed Core v7.0
# Main Controller


import datetime





try:
    from core_router import (
        route_message,
        router_status
    )
except Exception as e:

    route_message = None

    router_status = None

    print(
        "Router Error:",
        e
    )





try:
    from core_manager import (
        core_status
    )
except Exception:

    core_status = None





try:
    from self_diagnosis_engine import (
        diagnosis_status
    )
except Exception:

    diagnosis_status = None







SYSTEM_NAME = "Saeed Core"

VERSION = "7.0"








def process_message(

        message

):


    if route_message:


        try:


            return route_message(

                message

            )


        except Exception as e:


            return {


                "status":

                "error",


                "message":

                str(e)

            }




    return {


        "status":

        "offline",


        "message":

        "Router unavailable"

    }









def system_status():


    status = {


        "name":

        SYSTEM_NAME,


        "version":

        VERSION,


        "time":

        str(

            datetime.datetime.now()

        )

    }





    if router_status:


        status["router"] = router_status()






    if core_status:


        status["core"] = core_status()






    if diagnosis_status:


        status["diagnosis"] = diagnosis_status()





    return status







def start():


    print(

        SYSTEM_NAME,

        "started"

    )



    print(

        system_status()

    )







if __name__ == "__main__":


    start()



    while True:


        try:


            user_input = input(

                "\nUser: "

            )



            if user_input.lower() in [

                "exit",

                "quit",

                "خروج"

            ]:


                print(

                    "Saeed stopped"

                )


                break





            response = process_message(

                user_input

            )



            print(

                "\nSaeed:",

                response

            )





        except KeyboardInterrupt:


            break



        except Exception as e:


            print(

                "System Error:",

                e

            )
