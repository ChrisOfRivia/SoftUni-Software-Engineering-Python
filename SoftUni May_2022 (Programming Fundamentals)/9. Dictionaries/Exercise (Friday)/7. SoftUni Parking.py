registered_users = {}

n = int(input())

for commands in range(n):
    split = input().split(" ")
    code = ''
    if len(split) > 2:
        code = split[2]
    command = split[0]
    user = split[1]
    if command == 'register':
        if user not in registered_users:
            registered_users[user] = code
            print(f"{user} registered {code} successfully")
        else:
            print(f"ERROR: already registered with plate number {code}")

    elif command == 'unregister':
        if user not in registered_users:
            print(f"ERROR: user {user} not found")
        else:
            del registered_users[user]
            print(f"{user} unregistered successfully")

for users, license_plates in registered_users.items():
    print(f'{users} => {license_plates}')