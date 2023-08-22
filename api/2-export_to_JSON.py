#!/usr/bin/python3
"""Employee ID-based TODO List Progress"""


if __name__ == "__main__":
    import json
    import sys
    from urllib import request
    import json

    empid = sys.argv[1]

    url = request.urlopen("https://jsonplaceholder.typicode.com/users/{}"
                          .format(empid))

    data = json.loads(url.read().decode("utf-8"))

    url_task = request.urlopen(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(empid)
    )

    task = json.loads(url_task.read().decode("utf-8"))

    index = "{}".format(data["id"])
    dic_user = {index: []}

    for tasks in task:
        dic_user[index].append({
            "task": tasks["title"],
            "completed": tasks["completed"],
            "username": data["username"]
        })

    with open(f"{empid}.json", "w+") as file:
        file.write(json.dumps(dic_user))
        file.close()
