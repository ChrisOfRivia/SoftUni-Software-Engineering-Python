import re

text = input()

regex_words = r'(?P<whole_word>(?P<sep>::|\*\*)(?P<word>[A-Z][a-z]{2,})(?P=sep))|(?P<digits>\d)'

list_words = [word['whole_word'] for word in re.finditer(regex_words, text)]
list_digits = [digit['digits'] for digit in re.finditer(regex_words, text)]
while None in list_digits:
    list_digits.remove(None)
list_ints = [int(digit) for digit in list_digits]
while None in list_words:
    list_words.remove(None)

cool_words = []

cool_score = 1
for digits in list_ints:
    cool_score *= digits

for words in list_words:
    new = words[2:-2:]
    score = 0
    for char in new:
        score += ord(char)
    if score >= cool_score:
        cool_words.append(words)

print(f'Cool threshold: {cool_score}')
print(f'{len(list_words)} emojis found in the text. The cool ones are:')
for words in cool_words:
    print(f'{words}')