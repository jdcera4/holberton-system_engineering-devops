#!/usr/bin/python3
""" Module gether data from an API
"""
import requests
from sys import argv


if __name__ == "__main__":
    id_empl = int(argv[1])
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(id_empl)).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(id_empl)).json()
    tasks = []
    for task in todos:
        if task.get('completed') is True:
            tasks.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}): ".
          format(user.get('name'), len(tasks), len(todos)))
    for task in tasks:
        print("\t{}".format(task))
