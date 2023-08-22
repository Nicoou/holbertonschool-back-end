#!/usr/bin/python3
"""Employee ID-based TODO List Progress"""

if __name__ == "__main__":
    import json
    from urllib import request
    import csv
    import sys

    empid = sys.argv[1]

    url = request.urlopen("https://jsonplaceholder.typicode.com/users/{}"
                          .format(empid))

    data = json.loads(url.read().decode("utf-8"))

    url_task = request.urlopen(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(empid)
    )

    task = json.loads(url_task.read().decode("utf-8"))

    csv_filename = f"{empid}.csv"

    with open(csv_filename, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file, dialect="Dialect")
        csv_writer.writerow(
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        )

        for row in task:
            csv_writer.writerow(
                [row["userId"], data["name"], row["completed"], row["title"]]
            )
