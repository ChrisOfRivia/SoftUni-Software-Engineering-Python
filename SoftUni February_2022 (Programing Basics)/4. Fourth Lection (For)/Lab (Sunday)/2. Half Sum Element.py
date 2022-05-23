from sys import maxsize

n = int(input())

collect = 0
max_number = -maxsize
for i in range(n):
    num = int(input())

    collect += num
    if num > max_number:
        max_number = num

if collect - max_number == max_number:
        print("Yes")
        print(f"Sum = {collect - max_number}")

else:
        print("No")
        print(f"Diff = {abs(collect - max_number - max_number)}")