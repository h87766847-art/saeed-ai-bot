# upgrade_security.py
# Saeed Core v8.9
# Upgrade Security Layer


import os
import hashlib
import datetime





SECURITY_LOG = []






def calculate_hash(path):


    if not os.path.exists(path):

        return None



    sha = hashlib.sha256()



    with open(

        path,

        "rb"

    ) as file:


        while True:


            data = file.read(4096)


            if not data:

                break



            sha.update(data)



    return sha.hexdigest()







def check_file_exists(filename):


    return os.path.exists(filename)









def verify_package(manifest):


    result = {


        "valid":

        True,


        "checks":

        [],


        "time":

        str(datetime.datetime.now())

    }







    if not manifest:


        result["valid"] = False

        result["checks"].append(

            "manifest missing"

        )

        return result







    if "version" not in manifest:


        result["valid"] = False


        result["checks"].append(

            "version missing"

        )







    if "files" not in manifest:


        result["valid"] = False


        result["checks"].append(

            "files list missing"

        )







    for item in manifest.get(

        "files",

        []

    ):


        if "name" not in item:


            result["valid"] = False


            result["checks"].append(

                "file name missing"

            )






    SECURITY_LOG.append(

        result

    )



    return result







def verify_file_integrity(

    old_file,

    expected_hash

):


    current_hash = calculate_hash(

        old_file

    )



    return current_hash == expected_hash









def security_status():


    return {


        "checks":

        len(

            SECURITY_LOG

        ),


        "status":

        "active"

  }
