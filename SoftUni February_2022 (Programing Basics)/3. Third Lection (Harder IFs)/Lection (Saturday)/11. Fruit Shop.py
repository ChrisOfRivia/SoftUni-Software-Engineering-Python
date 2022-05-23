fruit = input()
day_of_week = input()
quantity = float(input())

price = 0

if fruit not in "banana, apple, orange, grapefruit, kiwi, pineapple, grapes" or day_of_week not in "Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday":
    print("error")

if day_of_week in "Saturday, Sunday":
    if fruit == "banana":
        price = 2.70
        print(f"{price * quantity:.2f}")
    elif fruit == "apple":
        price = 1.25
        print(f"{price * quantity:.2f}")
    elif fruit == "orange":
        price = 0.90
        print(f"{price * quantity:.2f}")
    elif fruit == "grapefruit":
        price = 1.60
        print(f"{price * quantity:.2f}")
    elif fruit == "kiwi":
        price = 3.00
        print(f"{price * quantity:.2f}")
    elif fruit == "pineapple":
        price = 5.60
        print(f"{price * quantity:.2f}")
    elif fruit == "grapes":
        price = 4.20
        print(f"{price * quantity:.2f}")
elif day_of_week in "Monday, Tuesday, Wednesday, Thursday, Friday":
    if fruit == "banana":
        price = 2.50
        print(f"{price * quantity:.2f}")
    elif fruit == "apple":
        price = 1.20
        print(f"{price * quantity:.2f}")
    elif fruit == "orange":
        price = 0.85
        print(f"{price * quantity:.2f}")
    elif fruit == "grapefruit":
        price = 1.45
        print(f"{price * quantity:.2f}")
    elif fruit == "kiwi":
        price = 2.70
        print(f"{price * quantity:.2f}")
    elif fruit == "pineapple":
        price = 5.50
        print(f"{price * quantity:.2f}")
    elif fruit == "grapes":
        price = 3.85
        print(f"{price * quantity:.2f}")


