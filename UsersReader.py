import json

with open('users.json', "r") as Users:
    users = json.loads(Users.read())

    users_list = users

    for user in users_list:
        print(user['name'], user['gender'], user['address'], user['age'])
