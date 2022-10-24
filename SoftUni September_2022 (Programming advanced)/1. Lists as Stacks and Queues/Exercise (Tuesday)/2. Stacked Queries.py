stack = []

n = int(input())

for query in range(n):
    number = input().split(' ')

    if number[0] == '1':
        actual_number = int(number[1])
        stack.append(actual_number)
    elif number[0] == '2':
        if stack:
            stack.pop()
    elif number[0] == '3':
        if stack:
            print(max(stack))
    elif number[0] == '4':
        if stack:
            print(min(stack))

top_to_bottom_stack = []

while stack:
    top_el = stack.pop()
    top_to_bottom_stack.append(str(top_el))

print(', '.join(top_to_bottom_stack))