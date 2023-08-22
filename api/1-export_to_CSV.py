#!/usr/bin/python3
"""Employee ID-based TODO List Progress"""

if __name__ == "__main__":
    import json
    from urllib import request
    import csv
    import sys

    empid = sys.argv[1]

    url = request.urlopen("https://jsonplaceholder.typicode.com/users/{}".
                          format(empid))

    data = json.loads(url.read().decode("utf-8"))

    url_task = request.urlopen(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(empid)
    )

    task = json.loads(url_task.read().decode("utf-8"))

    csv.register_dialect("Dialect", quoting=csv.QUOTE_ALL)
    with open(f"{empid}.csv", "w+") as file:
        writecsv = csv.writer(file, dialect="Dialect")
        for row in task:
            writecsv.writerow(
                [row["userId"], data["username"],
                 row["completed"], row["title"]]
            )
