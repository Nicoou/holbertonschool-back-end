#!/usr/bin/python3
"""Employee ID-based TODO List Progress"""

if __name__ == "__main__":
    import json
    import requests
    import csv
    import sys

    empid = sys.argv[1]

    url = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                          .format(empid))

    data = json.loads(url.text)

    url_task = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(empid)
    )

    task = json.loads(url_task.text)

    csv_filename = f"{empid}.csv"

    with open(csv_filename, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        csv_writer.writerow(
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        )

        for row in task:
            csv_writer.writerow(
                [row["userId"], data["name"], row["completed"], row["title"]]
            )
