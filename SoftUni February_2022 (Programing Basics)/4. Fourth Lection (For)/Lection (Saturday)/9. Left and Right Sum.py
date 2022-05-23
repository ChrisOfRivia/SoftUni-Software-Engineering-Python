n = int(input())

left_side = 0
right_side = 0

for i in range(n*2):
    number = int(input())
    if i < n:
        left_side += number
    else:
        right_side += number

if left_side == right_side:
    print(f"Yes, sum = {left_side}")
else:
    print(f"No, diff = {abs(left_side - right_side)}")

