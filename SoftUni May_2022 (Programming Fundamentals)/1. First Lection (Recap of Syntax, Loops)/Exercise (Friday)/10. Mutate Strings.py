first_string = input()
second_string = input()
last_string = ""

for times in range(1, len(first_string)):
    left_side = second_string[:times]
    right_side = first_string[times:]
    current_string = left_side + right_side
    if current_string != last_string:
        print(current_string)
    last_string = current_string