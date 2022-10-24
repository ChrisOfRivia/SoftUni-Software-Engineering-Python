numbers = input().split(" ")
remover = int(input())

list_numbers = []
list_string = []

delimeter = ", "
strings = ""

for integers in numbers:
    integers = int(integers)
    list_numbers.append(integers)

for num in range(remover):
    list_numbers.remove(min(list_numbers))

for i in list_numbers:
    strings = str(i)
    list_string.append(strings)

result = delimeter.join(list_string)
print(result)