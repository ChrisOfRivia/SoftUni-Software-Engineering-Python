from sys import maxsize

times = int(input())

no_even_min_max = False
no_nums_at_all = False

if 0 <= times < 2:
    no_even_min_max = True

odd_sum = 0
odd_min = maxsize
odd_max = -maxsize

even_sum = 0
even_min = maxsize
even_max = -maxsize

for each_num in range(1, times + 1):
    num = float(input())

    if each_num % 2 != 0:
        odd_sum += num

        if num > odd_max:
            odd_max = num

        if num < odd_min:
            odd_min = num
    elif each_num % 2 == 0:
        even_sum += num

        if num > even_max:
            even_max = num

        if num < even_min:
            even_min = num

if no_even_min_max:
    if times == 0:
        print(f"OddSum={odd_sum:.2f},")
        print(f"OddMin=No,")
        print(f"OddMax=No,")
        print(f"EvenSum={even_sum:.2f},")
        print(f"EvenMin=No,")
        print(f"EvenMax=No")
    else:
        print(f"OddSum={odd_sum:.2f},")
        print(f"OddMin={odd_min:.2f},")
        print(f"OddMax={odd_max:.2f},")
        print(f"EvenSum={even_sum:.2f},")
        print(f"EvenMin=No,")
        print(f"EvenMax=No")
else:
    print(f"OddSum={odd_sum:.2f},")
    print(f"OddMin={odd_min:.2f},")
    print(f"OddMax={odd_max:.2f},")
    print(f"EvenSum={even_sum:.2f},")
    print(f"EvenMin={even_min:.2f},")
    print(f"EvenMax={even_max:.2f}")
