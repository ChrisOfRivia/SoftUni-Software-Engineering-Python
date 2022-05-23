n = int(input())

counter = 1
counter_done = False

for columns in range(1, n + 1):
    for rows in range(1, columns + 1):
        print(counter, end=" ")
        counter += 1
        if counter > n:
            counter_done = True
            break
    if counter_done:
        break
    print()