from collections import deque

seats = input().split(', ')
first_num_seats = deque(map(int, input().split(', ')))
second_num_seats = deque(map(int, input().split(', ')))

rotations = 0
matches = []

while len(matches) < 3 and rotations < 10:
    first_num = first_num_seats[0]
    second_num = second_num_seats[-1]
    ascii_char = chr(first_num + second_num)

    first_combo = str(first_num) + str(ascii_char)
    second_combo = str(second_num) + str(ascii_char)

    no_equality = True

    for num_seat in seats:
        if num_seat == first_combo or num_seat == second_combo:
            first_num_seats.popleft()
            second_num_seats.pop()
            matches.append(num_seat)
            seats.remove(num_seat)
            no_equality = False
            rotations += 1
            break

    if no_equality:
        rotations += 1
        first_num_seats.rotate(-1)
        second_num_seats.rotate(1)

print(f"Seat matches: {', '.join(matches)}")
print(f"Rotations count: {rotations}")
