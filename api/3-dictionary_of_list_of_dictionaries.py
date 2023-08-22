#!/usr/bin/python3
"""Employee ID-based TODO List Progress"""

if __name__ == "__main__":
    import json
    from urllib import request
    import sys

    dic_user = {}
    url = request.urlopen(
        "https://jsonplaceholder.typicode.com/users/")

    data = json.loads(url.read().decode("utf-8"))

    url_task = request.urlopen(
        "https://jsonplaceholder.typicode.com/todos")
    task = json.loads(url_task.read().decode("utf-8"))

    for user in data:
        user_id = str(user["id"])
        user_tasks = [
            {
                "task": tasks["title"],
                "username": user["username"],
                "completed": tasks["completed"]
            }
            for tasks in task if tasks["userId"] == user["id"]
        ]
        dic_user[user_id] == user_tasks
        with open(f"todo_all_employees.json", "w+") as file:
          file.write(json.dumps(dic_user))
          file.close()
