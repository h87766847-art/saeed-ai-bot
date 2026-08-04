# project_scanner.py
# Saeed Core v7.6
# Project Scanner


import os
import datetime
import ast





SCAN_RESULT = {}







def scan_files(path="."):


    files = []



    for root, dirs, names in os.walk(path):


        for name in names:


            if name.endswith(".py"):


                files.append(

                    os.path.join(root, name)

                )



    return files







def check_imports(filename):


    imports = []



    try:


        with open(

            filename,

            "r",

            encoding="utf-8"

        ) as file:


            tree = ast.parse(

                file.read()

            )



        for node in ast.walk(tree):


            if isinstance(node, ast.Import):


                for item in node.names:


                    imports.append(

                        item.name

                    )



            elif isinstance(node, ast.ImportFrom):


                if node.module:


                    imports.append(

                        node.module

                    )



    except Exception as e:


        return {


            "error":

            str(e)

        }



    return imports







def run_scan(path="."):


    global SCAN_RESULT



    result = {


        "time":

        str(datetime.datetime.now()),


        "files":

        [],


        "count":

        0

    }



    files = scan_files(path)



    for file in files:


        result["files"].append({


            "name":

            file,


            "imports":

            check_imports(file)

        })



    result["count"] = len(files)



    SCAN_RESULT = result



    return result







def scanner_status():


    return {


        "files":

        SCAN_RESULT.get(

            "count",

            0

        ),


        "status":

        "ready"

    }
