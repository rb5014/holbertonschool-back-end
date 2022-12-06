#!/usr/bin/python3
"""export data in a csv file"""


import csv
import json
import requests
import sys
import urllib.request

if __name__ == "__main__":

    try:
        id = int(sys.argv[1])

    except Exception:
        exit

    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos?format=csv")
    employees = requests.get(
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

    with open(sys.argv[1] + '.csv', 'w', encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for row in row_list:
            writer.writerow(row)
