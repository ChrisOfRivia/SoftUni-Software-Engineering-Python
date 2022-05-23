sum_money = int(float(input()) * 100)

coins = 0

while True:

    if sum_money >= 200:
        sum_money -= 200
        coins += 1
        continue
    elif sum_money >= 100:
        sum_money -= 100
        coins += 1
        continue
    elif sum_money >= 50:
        sum_money -= 50
        coins += 1
        continue
    elif sum_money >= 20:
        sum_money -= 20
        coins += 1
        continue
    elif sum_money >= 10:
        sum_money -= 10
        coins += 1
        continue
    elif sum_money >= 5:
        sum_money -= 5
        coins += 1
        continue
    elif sum_money >= 2:
        sum_money -= 2
        coins += 1
        continue
    elif sum_money >= 1:
        sum_money -= 1
        coins += 1
        continue

    if sum_money <= 0:
        break

print(f"{coins}")