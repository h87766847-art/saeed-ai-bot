# security_engine.py
# Saeed Core
# Advanced Security Engine


import datetime
import hashlib



SECURITY_LOG = []


USERS = {}







def hash_data(data):


    return hashlib.sha256(

        data.encode("utf-8")

    ).hexdigest()







def create_user(

        username,

        role="user"

):


    USERS[username] = {


        "role":

        role,


        "created":

        str(

            datetime.datetime.now()

        ),


        "active":

        True

    }



    return True







def check_user(username):


    return USERS.get(

        username,

        None

    )








def set_permission(

        username,

        permission

):


    if username not in USERS:


        return False




    if "permissions" not in USERS[username]:


        USERS[username]["permissions"] = []





    USERS[username]["permissions"].append(

        permission

    )



    return True








def has_permission(

        username,

        permission

):


    user = USERS.get(

        username

    )



    if not user:


        return False




    return permission in user.get(

        "permissions",

        []

    )








def security_event(

        event,

        level="info"

):


    data = {


        "event":

        event,


        "level":

        level,


        "time":

        str(

            datetime.datetime.now()

        )

    }



    SECURITY_LOG.append(

        data

    )



    return data








def get_security_logs():


    return SECURITY_LOG







def security_status():


    return {


        "users":

        len(USERS),


        "logs":

        len(SECURITY_LOG),


        "status":

        "active"

    }
