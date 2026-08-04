# upgrade_reporter.py
# Saeed Core v8.8
# Upgrade Report Generator


import os
import json
import datetime





REPORT_FILE = "upgrade_reports.json"







def load_reports():


    if not os.path.exists(

        REPORT_FILE

    ):


        return []



    with open(

        REPORT_FILE,

        "r",

        encoding="utf-8"

    ) as file:


        return json.load(file)








def save_reports(data):


    with open(

        REPORT_FILE,

        "w",

        encoding="utf-8"

    ) as file:


        json.dump(

            data,

            file,

            ensure_ascii=False,

            indent=4

        )








def create_report(

    old_version,

    new_version,

    files,

    status,

    errors=None

):


    report = {


        "old_version":

        old_version,


        "new_version":

        new_version,


        "files":

        files,


        "status":

        status,


        "errors":

        errors or [],


        "time":

        str(datetime.datetime.now())

    }



    return report









def save_report(

    report

):


    reports = load_reports()



    reports.append(

        report

    )



    save_reports(

        reports

    )



    return report









def latest_report():


    reports = load_reports()



    if not reports:


        return None



    return reports[-1]









def report_status():


    return {


        "reports":

        len(

            load_reports()

        ),


        "status":

        "active"

    }
