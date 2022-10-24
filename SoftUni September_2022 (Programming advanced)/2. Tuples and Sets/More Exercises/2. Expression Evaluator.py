# "*", "+", "-", "/"

from math import floor
from collections import deque

number_queue = deque()

expression = input().split()
result = 0

for j in expression:
    if j.isdigit() or j[1:].isdigit():
        number_queue.append(int(j))
    elif j in ("*", "+", "-", "/"):
        initial_numbers = [str(el) for el in number_queue]
        if j == '*':
            while len(number_queue) > 1:
                first_number = number_queue.popleft()
                second_number = number_queue.popleft()
                result = first_number * second_number
                number_queue.appendleft(result)

        elif j == '+':
            while len(number_queue) > 1:
                first_number = number_queue.popleft()
                second_number = number_queue.popleft()
                result = first_number + second_number
                number_queue.appendleft(result)

        elif j == '-':
            while len(number_queue) > 1:
                first_number = number_queue.popleft()
                second_number = number_queue.popleft()
                result = first_number - second_number
                number_queue.appendleft(result)

        elif j == '/':
            while len(number_queue) > 1:
                first_number = number_queue.popleft()
                second_number = number_queue.popleft()
                result = floor(first_number / second_number)
                number_queue.appendleft(result)

print(result)