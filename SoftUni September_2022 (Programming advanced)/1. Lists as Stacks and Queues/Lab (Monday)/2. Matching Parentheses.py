algorithm = input()

stack_parentheses = []

for idx, ch in enumerate(algorithm):
    if ch == '(':
        stack_parentheses.append(idx)
    elif ch == ')':
        last_opening_bracket = stack_parentheses.pop()
        print(algorithm[last_opening_bracket:idx + 1])


