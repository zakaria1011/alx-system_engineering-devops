#!/usr/bin/python3
"""Export data in JSON format for all tasks from all employees."""
import csv
import json
import requests
import sys


if __name__ == "__main__":
    users = requests.get(
        'https://jsonplaceholder.typicode.com/users').json()
    todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos').json()

    all_employee_tasks = {}
    for user in users:
        employee_id = user['id']
        username = user['username']
        user_tasks = [{"username": username, "task": todo['title'],
                       "completed": todo['completed']}
                      for todo in todos if todo['userId'] == employee_id]
        all_employee_tasks[str(employee_id)] = user_tasks

    json_data = json.dumps(all_employee_tasks)
    with open('todo_all_employees.json', 'w') as jsonfile:
        jsonfile.write(json_data)
