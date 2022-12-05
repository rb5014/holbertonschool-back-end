#!/usr/bin/python3
"""Module to fetch data from url"""


import urllib.request
import json
import sys


if __name__ == "__main__":

    try:
        id = int(sys.argv[1])

    except Exception:
        exit

    todos = urllib.request.urlopen(
        "https://jsonplaceholder.typicode.com/todos")
    employees = urllib.request.urlopen(
        "https://jsonplaceholder.typicode.com/users")

    todos = json.loads(todos.read())
    employees = json.loads(employees.read())

    name = ""
    nb_done = 0
    total_tasks = 0
    title_list = []

    for employee in employees:
        if id == employee["id"]:
            name = employee["name"]

    for todo in todos:
        if todo["userId"] == id:
            total_tasks += 1
            if todo["completed"] is True:
                nb_done += 1
                title_list.append(todo["title"])
    print("Employee {} is done with tasks({}/{}):"
          .format(name, nb_done, total_tasks))

    for title in title_list:
        print("\t {}".format(title))
