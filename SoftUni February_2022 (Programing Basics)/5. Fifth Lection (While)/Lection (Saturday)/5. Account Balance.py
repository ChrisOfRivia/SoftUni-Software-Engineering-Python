No_More_Money = False

sum_num = 0

while not No_More_Money:
    number = input()

    if number == "NoMoreMoney":
        No_More_Money = True

    elif float(number) < 0:
        print("Invalid operation!")
        No_More_Money = True

    else:
        print(f"Increase: {float(number):.2f}")
        sum_num += float(number)


print(f"Total: {sum_num:.2f}")


