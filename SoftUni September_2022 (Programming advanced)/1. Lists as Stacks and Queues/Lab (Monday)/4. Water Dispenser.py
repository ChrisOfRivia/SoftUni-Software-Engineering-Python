from collections import deque

liters_in_tank = int(input())

queue = deque()

while True:
    person = input()
    if person == 'Start':
        break
    queue.append(person)

while True:
    action = input()
    if action == 'End':
        print(f'{liters_in_tank} liters left')
        break

    action = action.split(" ")

    if len(action) == 1:
        action = ''.join(action)
        action = int(action)
        person_getting_water = queue.popleft()
        if action <= liters_in_tank:
            liters_in_tank -= action
            print(f"{person_getting_water} got water")
        else:
            print(f'{person_getting_water} must wait')
    else:
        liters_in_tank += int(action[1])
