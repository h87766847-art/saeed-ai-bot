# core_manager.py
# Saeed Core v7.5
# Central Core Management


import datetime





try:
    from capability_manager import capability_status
except Exception:
    capability_status = None


try:
    from plugin_manager import plugin_status
except Exception:
    plugin_status = None


try:
    from api_bridge import bridge_status
except Exception:
    bridge_status = None


try:
    from module_loader import loader_status
except Exception:
    loader_status = None


try:
    from self_upgrade_engine import upgrade_status
except Exception:
    upgrade_status = None





COMPONENTS = {}







def register_component(

        name,

        status="active"

):


    COMPONENTS[name] = {


        "status":

        status,


        "time":

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


        return True



    return False







def get_components():


    return COMPONENTS







def system_health():


    return {


        "components":

        COMPONENTS,


        "capabilities":

        capability_status()

        if capability_status

        else None,


        "plugins":

        plugin_status()

        if plugin_status

        else None,


        "bridge":

        bridge_status()

        if bridge_status

        else None,


        "modules":

        loader_status()

        if loader_status

        else None,


        "upgrades":

        upgrade_status()

        if upgrade_status

        else None,


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

            COMPONENTS

        ),


        "status":

        "online"

    }







for component in [

    "brain",

    "memory",

    "router",

    "learning",

    "upgrade",

    "security",

    "plugins",

    "api"

]:


    register_component(

        component

)
