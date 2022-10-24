from collections import deque

chocolates = list(map(int, input().split(', ')))
cups_of_milk = deque(map(int, input().split(', ')))
milkshakes = 0

while milkshakes < 5 and chocolates and cups_of_milk:
    flag = False

    if chocolates[-1] <= 0:
        chocolates.pop()
        flag = True

    if cups_of_milk[0] <= 0:
        cups_of_milk.popleft()
        flag = True

    if flag:
        continue

    if chocolates[-1] == cups_of_milk[0]:
        milkshakes += 1
        chocolates.pop()
        cups_of_milk.popleft()
    else:
        cups_of_milk.append(cups_of_milk.popleft())
        chocolates[-1] -= 5

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print(f"Not enough milkshakes.")

print(f'Chocolate: {", ".join(map(str, chocolates)) if chocolates else "empty"}')
print(f'Milk: {", ".join(map(str, cups_of_milk)) if cups_of_milk else "empty"}')
