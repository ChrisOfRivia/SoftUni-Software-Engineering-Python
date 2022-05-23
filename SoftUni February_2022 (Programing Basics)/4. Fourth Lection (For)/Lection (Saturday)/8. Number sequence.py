from sys import maxsize

max_number = -maxsize
min_number = maxsize

n = int(input())

for i in range(n):
    nums = int(input())
    if nums > max_number:
        max_number = nums

    if nums < min_number:
        min_number = nums

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")