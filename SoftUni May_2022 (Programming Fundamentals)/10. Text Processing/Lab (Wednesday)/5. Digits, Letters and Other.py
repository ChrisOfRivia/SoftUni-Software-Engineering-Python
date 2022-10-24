letters = []
numbers = []
other = []

long_string = input()

for every_char in long_string:
    if every_char.isalpha():
        letters.append(every_char)
    elif every_char.isnumeric():
        numbers.append(every_char)
    else:
        other.append(every_char)

print(*numbers, sep="")
print(*letters, sep="")
print(*other, sep="")