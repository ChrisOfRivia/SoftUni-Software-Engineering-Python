first = input()
second = input()

for i in range(len(first)):
    if second[i] != first[i]:
        print(second[:i + 1] + first[i + 1:])