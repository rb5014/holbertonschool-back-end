#!/usr/bin/python3
"""export data in a json file"""


import json
import requests
import sys


if __name__ == "__main__":

    try:
        id = int(sys.argv[1])

    except Exception:
        exit

    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos?format=csv")
    employees = requests.get(
        "https://jsonplaceholder.typicode.com/users?format=csv")

    todos = todos.json()
    employees = employees.json()

    res_dict = {}
    username = ""
    for employee in employees:
        res_dict[str(employee["id"])] = []
        username = employee["username"]
        for todo in todos:
            if todo["userId"] == employee["id"]:
                d = {}
                d["username"] = username
                d["task"] = todo["title"]
                d["completed"] = todo["completed"]
                res_dict[str(employee["id"])].append(d)

    with open('todo_all_employees.json', 'w') as json_file:
        json_file.write(json.dumps(res_dict))
