import string

string1 = input()

for letters in string1:
    if letters in string.ascii_uppercase:
        print(f'{string1.index(letters)}', end="")