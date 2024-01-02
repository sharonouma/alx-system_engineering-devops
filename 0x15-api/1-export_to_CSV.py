
#!/usr/bin/python3

"""
accessing a url with employee ID to return information
"""


if __name__ == "__main__":
    """
    function to export the data into
    csv file
    """
    import csv
    import requests
    import sys
    ID = int(sys.argv[1])
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(ID)).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(ID)).json()
    with open("{}.csv".format(ID), 'w') as file:
        filler = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        for task in todo:
            filler.writerow([ID, user.get('username'),
                            task.get('completed'), task.get('title')])
