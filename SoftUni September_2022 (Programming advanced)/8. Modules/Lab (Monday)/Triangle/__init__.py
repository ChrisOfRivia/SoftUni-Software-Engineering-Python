def num_triangle(number):
    # pattern = ''
    for i in range(1, number + 1):
        for l in range(i):
            print(l + 1, end='')
        print()

    for j in range(number - 1, 0, -1):
        for m in range(j):
            print(m + 1, end='')
        print()

