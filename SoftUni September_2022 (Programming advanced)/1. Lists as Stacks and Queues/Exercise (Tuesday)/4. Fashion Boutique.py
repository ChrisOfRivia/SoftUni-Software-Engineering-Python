from collections import deque

sequence_of_integers = input().split(" ")
int_clothes = [int(el) for el in sequence_of_integers]
single_rack_capacity = int(input())

rack = deque()

sum_of_clothes = 0
rack.appendleft(sum_of_clothes)

while int_clothes:
    while sum_of_clothes < single_rack_capacity:
        if not int_clothes:
            break
        current_clothing = int_clothes.pop()
        sum_of_clothes += current_clothing
        rack[0] += current_clothing

        if rack[0] == single_rack_capacity:
            sum_of_clothes = 0
            if int_clothes:
                rack.appendleft(0)
            else:
                break
        elif rack[0] > single_rack_capacity:
            rack[0] -= current_clothing
            sum_of_clothes = 0
            rack.appendleft(current_clothing)

print(len(rack))
