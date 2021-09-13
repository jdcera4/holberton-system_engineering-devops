#!/usr/bin/python3
""" export data in the JSON format
"""
import csv
import requests
from sys import argv as av


if __name__ == "__main__":
    id_empl = int(av[1])
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(id_empl)).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(id_empl)).json()
    # List of list all data I need export
    data = {
        av[1]:
        [
            {
                'task': task.get('title'),
                'completed': task.get('completed'),
                'username': user['username']
            } for task in todos
        ]
    }
    # file name
    file = '{}.json'.format(av[1])
    # Write export file.json
    with open(file, 'w') as f:
        json.dump(data, f)
