# core_manager.py
# Saeed Core v7.5
# Central Core Manager


import datetime





try:

    from capability_manager import capability_status

except Exception:

    capability_status = None





try:

    from self_upgrade_engine import upgrade_status

except Exception:

    upgrade_status = None





try:

    from module_loader import loader_status

except Exception:

    loader_status = None






COMPONENTS = {}







def register_component(

        name,

        status="active"

):


    COMPONENTS[name] = {


        "status":

        status,


        "registered":

        str(

            datetime.datetime.now()

        )

    }



    return True







def update_component(

        name,

        status

):


    if name in COMPONENTS:


        COMPONENTS[name]["status"] = status


        COMPONENTS[name]["updated"] = str(

            datetime.datetime.now()

        )


        return True



    return False







def get_components():


    return COMPONENTS







def system_health():


    health = {


        "components":

        COMPONENTS,


        "time":

        str(

            datetime.datetime.now()

        )

    }



    if capability_status:


        health["capabilities"] = capability_status()





    if upgrade_status:


        health["upgrades"] = upgrade_status()





    if loader_status:


        health["modules"] = loader_status()





    return health







def core_status():


    return {


        "name":

        "Saeed Core Manager",


        "components":

        len(

            COMPONENTS

        ),


        "status":

        "online"

    }







for item in [

    "brain",

    "memory",

    "router",

    "learning",

    "upgrade",

    "security",

    "plugins"

]:


    register_component(

        item

)
