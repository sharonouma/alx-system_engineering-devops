#!/usr/bin/python3

"""
accessing a url with employee ID to return information
"""


if __name__ == "__main__":
    import json
    import requests
    import sys
    ID = int(sys.argv[1])
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(ID)).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?ID={}".
                        format(ID)).json()
    username = user.get('username')
    tasks = []
    for task in todo:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = username
        tasks.append(task_dict)
    json_file = {}
    json_file[ID] = tasks
    with open("{}.json".format(ID), 'w') as file:
        json.dump(json_file, file)
