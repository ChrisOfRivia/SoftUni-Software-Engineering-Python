from collections import deque

cups_capacity = input().split(" ")
filled_bottles = input().split(" ")

cups = [int(el) for el in cups_capacity]
bottles = [int(el) for el in filled_bottles]

cups = deque(cups)
bottles = deque(bottles)

wasted_liters = 0

while True:
    if bottles and cups:
        last_bottle = bottles[-1]
        first_cup = cups[0]
        if last_bottle >= first_cup:
            cups.popleft()
            bottles[-1] -= first_cup
            wasted_liters += bottles.pop()
        elif last_bottle < first_cup:
            bottles.pop()
            while last_bottle < first_cup:
                last_bottle += bottles.pop()
            cups.popleft()
            wasted_liters += last_bottle - first_cup
    else:
        if not cups and bottles:
            bottles_str = [str(el) for el in bottles]
            print(f'Bottles: {" ".join(bottles_str)}')
            print(f'Wasted litters of water: {wasted_liters}')
            break
        elif cups and not bottles:
            cups_str = [str(el) for el in cups]
            print(f"Cups: {(' '.join(cups_str))}")
            print(f"Wasted litters of water: {wasted_liters}")
            break



