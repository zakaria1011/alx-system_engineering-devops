#!/usr/bin/python3
""" api todo"""
import csv
import json
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(employee_id))
    user_data = user.json()
    name = user_data.get("username")
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    user_todos = [todo for todo in todos if todo['userId'] == int(employee_id)]
    json_data = {employee_id: [{"task": todo['title'],
                                "completed": todo['completed'],
                                "username": name} for todo in user_todos]}
    json_file_name = '{}.json'.format(employee_id)
    with open(json_file_name, 'w') as jsonfile:
        json.dump(json_data, jsonfile)
