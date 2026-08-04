# core_manager.py
# Saeed Core v7.5
# Central System Manager


import datetime





SYSTEM_COMPONENTS = {}







def register_component(

        name,

        component,

        status="active"

):


    SYSTEM_COMPONENTS[name] = {


        "component":

        component,


        "status":

        status,


        "registered":

        str(

            datetime.datetime.now()

        )

    }



    return True







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







def get_component(

        name

):


    return SYSTEM_COMPONENTS.get(

        name,

        None

    )








def list_components():


    return SYSTEM_COMPONENTS







def register_core_modules():


    modules = [


        "brain",


        "memory",


        "router",


        "learning",


        "upgrade",


        "security",


        "plugins"

    ]



    for module in modules:


        register_component(

            module,

            module,

            "active"

        )



    return True







def system_health():


    total = len(

        SYSTEM_COMPONENTS

    )



    active = 0



    for item in SYSTEM_COMPONENTS.values():


        if item["status"] == "active":


            active += 1





    return {


        "components":

        total,


        "active":

        active,


        "health":

        "excellent"

        if total == active

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


        "components":

        len(

            SYSTEM_COMPONENTS

        ),


        "health":

        system_health(),


        "status":

        "online"

    }






register_core_modules()
