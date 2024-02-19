#!/usr/bin/python3
""" api todos """
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(employee_id))
    name = user.json().get('name')
    data = requests.get('https://jsonplaceholder.typicode.com/todos')

    todos = data.json()
    tasks = 0
    completed_tasks = []

    for todo in todos:
        if (todo['userId'] == int(employee_id)):
            tasks += 1
            if (todo['completed']):
                tasks += 1
                completed_tasks.append(todo["title"])

    print('Employee {} is done with tasks({}/{}):'
          .format(name, len(completed_tasks), tasks - len(completed_tasks)))
    for title in completed_tasks:
        print("\t {}".format(title))
