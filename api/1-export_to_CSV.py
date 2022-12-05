#!/usr/bin/python3
"""Using what you did in the task #0, extend your Python script to export
data in the CSV format.

Requirements:

Records all tasks that are owned by this employee
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv"""

import urllib.request
import json
import csv
import sys

try:
    id = int(sys.argv[1])

except Exception:
    exit

todos = urllib.request.urlopen(
    "https://jsonplaceholder.typicode.com/todos?format=csv")
employees = urllib.request.urlopen(
    "https://jsonplaceholder.typicode.com/users?format=csv")

todos = json.loads(todos.read())
employees = json.loads(employees.read())

username = ""
for employee in employees:
    if employee["id"] == id:
        username = employee["username"]

row_list = []
for todo in todos:
    if todo["userId"] == id:
        fields = [id, username, todo["completed"], todo["title"]]
        row_list.append(fields)

with open(sys.argv[1] + '.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',', quotechar='"',
                        quoting=csv.QUOTE_ALL)
    for row in row_list:
        writer.writerow(row)
