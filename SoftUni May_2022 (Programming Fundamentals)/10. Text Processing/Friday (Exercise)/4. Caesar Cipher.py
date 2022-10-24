text = input()

for word in text:
    print(chr(ord(word) + 3), end="")