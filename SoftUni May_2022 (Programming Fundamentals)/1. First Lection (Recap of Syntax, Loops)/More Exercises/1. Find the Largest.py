number = int(input())

list1 = list(str(number))
list1.sort()
no_brackets = "".join(list1)

print((no_brackets[::-1]))



