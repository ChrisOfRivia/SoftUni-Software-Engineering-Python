command = input()

while command != "Welcome!":
    if command == "Voldemort":
        print(f"You must not speak of that name!")
        continue
    if len(command) < 5:
        print(f"{command} goes to Gryffindor.")
    elif len(command) == 5:
        print(f"{command} goes to Slytherin.")
    elif len(command) == 6:
        print(f"{command} goes to Ravenclaw.")
    elif len(command) > 6:
        print(f"{command} goes to Hufflepuff.")
    command = input()
print(f"Welcome to Hogwarts.")