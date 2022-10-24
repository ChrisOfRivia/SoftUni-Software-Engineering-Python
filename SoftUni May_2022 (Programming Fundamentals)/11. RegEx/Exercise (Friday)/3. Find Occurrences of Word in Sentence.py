import re

text = input()

word = input()

word = "\\b"+word+"\\b"

result = re.findall(word, text, re.IGNORECASE)

print(len(result))