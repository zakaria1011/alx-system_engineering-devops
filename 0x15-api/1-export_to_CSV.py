#!/usr/bin/python3
""" api todo"""
import csv
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
    csv_file_name = '{}.csv'.format(employee_id)
    with open(csv_file_name, 'w', newline="") as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in user_todos:
            csv_writer.writerow([employee_id, name, todo['completed'], todo['title']])
