# core_manager.py
# Saeed Core
# Central Core Management System


import datetime





SYSTEM_COMPONENTS = {}







def register_component(

        name,

        component

):


    SYSTEM_COMPONENTS[name] = {


        "component":

        component,


        "status":

        "registered",


        "time":

        str(

            datetime.datetime.now()

        )

    }



    return True








def get_component(

        name

):


    if name in SYSTEM_COMPONENTS:


        return SYSTEM_COMPONENTS[name]



    return None







def update_component_status(

        name,

        status

):


    if name in SYSTEM_COMPONENTS:


        SYSTEM_COMPONENTS[name]["status"] = status


        SYSTEM_COMPONENTS[name]["updated"] = str(

            datetime.datetime.now()

        )


        return True



    return False







def list_components():


    return SYSTEM_COMPONENTS







def system_health():


    total = len(

        SYSTEM_COMPONENTS

    )


    active = 0



    for component in SYSTEM_COMPONENTS.values():


        if component["status"] in [

            "registered",

            "active"

        ]:


            active += 1





    return {


        "components":

        total,


        "active":

        active,


        "health":

        "good"

        if active == total

        else "warning",


        "time":

        str(

            datetime.datetime.now()

        )

    }








def core_status():


    return {


        "name":

        "Saeed Core Manager",


        "status":

        "online",


        "components":

        len(SYSTEM_COMPONENTS)

  }
