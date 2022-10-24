initial_route = input()
route_list_char = []
for char in initial_route:
    route_list_char.append(char)

while True:
    command = input().split(":")
    if command[0] == 'Travel':
        break

    elif command[0] == 'Add Stop':
        index = int(command[1])
        string = command[2]
        if len(route_list_char) > index:
            for i, sym in enumerate(string):
                route_list_char.insert(index + i, sym)
        print(''.join(route_list_char))

    elif command[0] == 'Remove Stop':
        start_index = int(command[1])
        end_index = int(command[2])
        if len(route_list_char) > start_index and len(route_list_char) > end_index:
            route_list_char = [alpha for num, alpha in enumerate(route_list_char) if
                               num < start_index or num > end_index]
        print(''.join(route_list_char))
    elif command[0] == 'Switch':
        old_str = command[1]
        new_str = command[2]
        route_list_char = ''.join(route_list_char)
        route_list_char = route_list_char.replace(old_str, new_str)
        print(route_list_char)

if type(route_list_char) == list:
    route_list_char = ''.join(route_list_char)

print(f'Ready for world tour! Planned stops: {route_list_char}')
