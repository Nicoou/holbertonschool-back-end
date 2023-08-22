#!/usr/bin/python3
"""Employee ID-based TODO List Progress"""

if __name__ == "__main__":
    import json
    from urllib import request
    import csv
    import sys

    empid = sys.argv[1]

    url = request.urlopen(
        "https://jsonplaceholder.typicode.com/users/{}".format(empid))

    data = json.loads(url.read().decode("utf-8"))

    url_task = request.urlopen(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(empid)
    )
    tasks = json.loads(url_task.read().decode("utf-8"))

    index = "{}".format(data["id"])
    dic_user = {
        index: []
    }
    for task in tasks:
        dic_user[index].append({
            "task": task["title"],
            "completed": task["completed"],
            "username": data["username"],
        })

    with open(f"{empid}.json", "w+") as file:
        file.write(json.dumps(dic_user))
        file.close()
