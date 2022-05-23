from sys import maxsize

min_number = maxsize

while True:
    num = input()

    if num == "Stop":
        break
    else:
        num = int(num)
        if num < min_number:
            min_number = num

print(min_number)