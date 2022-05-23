floors = int(input())
rooms = int(input())

letter_room = ""
number = 0

for each_floor in range(floors * 10, 0, -10):
    for each_room in range(1, rooms + 1):
        if each_floor == floors * 10:
            letter_room = "L"
            if each_room < 2:
                number = each_floor
            print(f"{letter_room}{number} ", end="")
            number += 1
        elif (each_floor / 10) % 2 == 0:
            letter_room = "O"
            if each_room < 2:
                number = each_floor
            print(f"{letter_room}{number} ", end="")
            number += 1
        elif (each_floor / 10) % 2 != 0:
            letter_room = "A"
            if each_room < 2:
                number = each_floor
            print(f"{letter_room}{number} ", end="")
            number += 1
    print()