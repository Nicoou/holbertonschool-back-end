#!/usr/bin/python3
"""
This a Python script that for a given employee ID
      returns information about his/her TODO list progress.
"""

if __name__ == "__main__":
    import requests
    import sys

    empid = sys.argv[1]

    data = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(empid)
    ).json()

    task = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(empid)
    ).json()

    complete = list(filter(lambda task: task["completed"], task))

    print(
        "Employee {} is done with tasks({}/{})):".format(
            data["name"], len(complete), len(task)
        )
    )
    title = [task["title"] for task in complete]
    for text in title:
        print("\t {}".format(text))
