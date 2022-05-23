# За всеки четен ден и нечетен час, паркингът таксува 2.50 лева.
# Във всеки нечетен ден и четен час таксата е 1.25 лева,
# във всички останали случаи се заплаща 1 лев
# Таксуването става на всеки изминал час от деня.
# Всеки един от изходите трябва да бъде закръглен до втория знак след десетичната запетая.

num_days = int(input())
num_hours = int(input())

parking = 0
total = 0

for each_day in range(1, num_days + 1):
    for each_hour in range(1, num_hours + 1):
        if each_day % 2 != 0 and each_hour % 2 != 0:
            parking += 1

        elif each_day % 2 == 0 and each_hour % 2 == 0:
            parking += 1

        elif each_day % 2 == 0 and each_hour % 2 != 0:
            parking += 2.50

        elif each_day % 2 != 0 and each_hour % 2 == 0:
            parking += 1.25

    print(f"Day: {each_day} - {parking:.2f} leva")
    total += parking
    parking = 0
print(f"Total: {total:.2f} leva")