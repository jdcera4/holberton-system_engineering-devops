#!/usr/bin/python3
""" Module gether data from an API
"""
import csv
import requests
from sys import argv as av


if __name__ == "__main__":
    id_empl = int(av[1])
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(id_empl)).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(id_empl)).json()
    row = [
        [
            id_empl,
            user.get('username'),
            task.get('completed'),
            task.get('title')
        ] for task in todos
    ]

    file = '{}.csv'.format(av[1])
    # Write export file.csv
    with open(file, 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(row)
