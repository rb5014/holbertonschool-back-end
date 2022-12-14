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

    username = ""
    for employee in employees:
        if employee["id"] == id:
            username = employee["username"]

    res_dict = {str(id): []}
    for todo in todos:
        if todo["userId"] == id:
            d = {}
            d["task"] = todo["title"]
            d["completed"] = todo["completed"]
            d["username"] = username
            res_dict[str(id)].append(d)

    with open(sys.argv[1] + '.json', 'w') as json_file:
        json_file.write(json.dumps(res_dict))
