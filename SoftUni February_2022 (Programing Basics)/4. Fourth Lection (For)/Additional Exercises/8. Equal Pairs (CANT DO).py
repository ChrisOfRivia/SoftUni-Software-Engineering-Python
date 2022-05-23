num_doubles = int(input())

double = 0
first_num = 0
add = 0
success = False

for each_double in range(num_doubles * 2):
    num = int(input())
    double += num

    if each_double % 2 != 0:
        first_num += double
        if first_num % double == 0:
            success = True


if success:
    print(f"Yes, value={int(double / num_doubles)}")
else:
    max_diff = abs(first_num - double)
    print(f"No, maxdiff={max_diff}")




