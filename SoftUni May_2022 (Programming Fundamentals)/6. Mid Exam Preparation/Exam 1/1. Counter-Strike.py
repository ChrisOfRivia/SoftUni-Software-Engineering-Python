initial_energy = int(input())
battle_counter = 0

while True:
    command = input()
    if command == 'End of battle':
        print(f"Won battles: {battle_counter}. Energy left: {initial_energy}" )
        break
    else:
        command = int(command)

    if initial_energy >= command:
        initial_energy -= command
        battle_counter += 1
        if battle_counter % 3 == 0:
            initial_energy += battle_counter

    else:
        print(f"Not enough energy! Game ends with {battle_counter} won battles and {initial_energy} energy")
        break
