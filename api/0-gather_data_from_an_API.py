#!/usr/bin/python3
"""
This a Python script that for a given employee ID
      returns information about his/her TODO list progress.
"""

if __name__ == "__main__":
    import requests
    import sys

    Idemp = sys.argv[1]

    data = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(Idemp)
    ).json()

    task = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(Idemp)
    ).json()

    complet = list(filter(lambda task: task["complet"], task))

    print(
        "Employee {} is done with tasks({}/{})):".format(
            data["name"], len(complet), len(task)
        )
    )

    title = [task["title"] for task in complet]
    for text in title:
        print("\t {}".format(text))
