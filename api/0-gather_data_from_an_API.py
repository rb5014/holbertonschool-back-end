#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.

Requirements:

You must use urllib or requests module
The script must accept an integer as a parameter, which is the employee ID
The script must display on the standard output the employee TODO list progress
in this exact format:
First line: Employee EMPLOYEE_NAME is done with
tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
EMPLOYEE_NAME: name of the employee
NUMBER_OF_DONE_TASKS: number of completed tasks
TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of completed
and non-completed tasks
Second and N next lines display the title of completed tasks:
TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)"""

import urllib.request
import json
import sys

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
