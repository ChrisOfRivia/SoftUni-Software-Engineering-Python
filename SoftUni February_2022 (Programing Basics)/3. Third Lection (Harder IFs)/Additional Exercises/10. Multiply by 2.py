num = float(input())

while True:
    if num < 0:
        print(f"Negative number!")
        break
    else:
        float_num = float(num * 2)
        print(f"Result: {float_num:.2f}")
    num = float(input())