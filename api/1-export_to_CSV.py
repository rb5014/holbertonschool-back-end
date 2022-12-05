#!/usr/bin/python3
"""export data in a csv file"""


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
