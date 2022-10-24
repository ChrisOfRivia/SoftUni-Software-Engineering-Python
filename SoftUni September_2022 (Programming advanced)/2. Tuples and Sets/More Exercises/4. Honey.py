from collections import deque

working_bees = deque(map(int, input().split()))
nectar = list(map(int, input().split()))
sequence_symbols = deque(input().split())

collected_nectar = 0

while working_bees and nectar:
    first_bee = working_bees[0]
    last_nectar = nectar[-1]

    if last_nectar >= first_bee:
        if sequence_symbols[0] == '+':
            collected_nectar += abs(first_bee + last_nectar)
        elif sequence_symbols[0] == '-':
            collected_nectar += abs(first_bee - last_nectar)
        elif sequence_symbols[0] == '/':
            if last_nectar == 0:
                collected_nectar += 0
            else:
                collected_nectar += abs(first_bee / last_nectar)
        elif sequence_symbols[0] == '*':
            collected_nectar += abs(first_bee * last_nectar)
        sequence_symbols.popleft()
        working_bees.popleft()
        nectar.pop()

    elif last_nectar < first_bee:
        nectar.pop()

print(f'Total honey made: {collected_nectar}')
if working_bees:
    print(f'Bees left: {", ".join(map(str, working_bees))}')
if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")