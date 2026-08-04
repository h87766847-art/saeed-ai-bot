# plugin_manager.py
# Saeed Core
# Advanced Plugin Management System


import datetime
import uuid





PLUGINS = {}







def register_plugin(

        name,

        module,

        description=""

):


    plugin_id = str(

        uuid.uuid4()

    )



    PLUGINS[plugin_id] = {


        "id":

        plugin_id,


        "name":

        name,


        "module":

        module,


        "description":

        description,


        "enabled":

        True,


        "created":

        str(

            datetime.datetime.now()

        )

    }



    return PLUGINS[plugin_id]








def enable_plugin(

        plugin_id

):


    if plugin_id in PLUGINS:


        PLUGINS[plugin_id]["enabled"] = True


        return True



    return False







def disable_plugin(

        plugin_id

):


    if plugin_id in PLUGINS:


        PLUGINS[plugin_id]["enabled"] = False


        return True



    return False







def get_plugins():


    return list(

        PLUGINS.values()

    )








def get_active_plugins():


    return [

        plugin

        for plugin in PLUGINS.values()

        if plugin["enabled"]

    ]








def remove_plugin(

        plugin_id

):


    if plugin_id in PLUGINS:


        del PLUGINS[plugin_id]


        return True



    return False







def plugin_status():


    return {


        "total":

        len(PLUGINS),


        "active":

        len(

            get_active_plugins()

        ),


        "status":

        "online"

  }
