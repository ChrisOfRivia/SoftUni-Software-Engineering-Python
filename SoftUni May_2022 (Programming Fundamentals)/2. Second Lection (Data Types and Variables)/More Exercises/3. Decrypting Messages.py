key = int(input())
lines = int(input())

word = ""

for codes in range(lines):
    letter = input()
    ascii_number = ord(letter)
    ascii_letter = chr(ascii_number + key)
    word += ascii_letter
print(word)