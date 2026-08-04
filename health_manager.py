# health_manager.py
# Saeed Core v7.6
# System Health Manager


import datetime





try:
    from file_monitor import monitor_status
except Exception:
    monitor_status = None


try:
    from event_engine import event_status
except Exception:
    event_status = None


try:
    from system_logger import logger_status
except Exception:
    logger_status = None


try:
    from plugin_manager import plugin_status
except Exception:
    plugin_status = None







def collect_health():


    health = {


        "time":

        str(datetime.datetime.now()),


        "system":

        "online"

    }



    if monitor_status:


        health["files"] = monitor_status()



    if event_status:


        health["events"] = event_status()



    if logger_status:


        health["logger"] = logger_status()



    if plugin_status:


        health["plugins"] = plugin_status()



    return health







def health_check():


    data = collect_health()



    warnings = []



    for key, value in data.items():


        if isinstance(value, dict):


            if value.get("status") == "warning":


                warnings.append(key)



    return {


        "healthy":

        len(warnings) == 0,


        "warnings":

        warnings,


        "details":

        data

    }







def health_status():


    result = health_check()



    return {


        "status":

        "healthy"

        if result["healthy"]

        else "warning",


        "warnings":

        len(result["warnings"])

    }
