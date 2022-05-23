from sys import maxsize

max_number = -maxsize

while True:
    num = input()

    if str(num) == "Stop":
        break
    else:
        num = int(num)
        if int(num) > max_number:
            max_number = num


print(max_number)