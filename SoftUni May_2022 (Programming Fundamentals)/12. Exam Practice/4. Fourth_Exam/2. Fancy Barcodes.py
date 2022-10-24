import re

n = int(input())

all_words = []
valid_words = []
invalid_words = []

for j in range(n):
    word = input()
    all_words.append(word)

regex = r'(\@(\#{1,})(?P<word>[A-Z][A-Za-z0-9]{4,}[A-Z])\@(\#{1,}))'

match = re.findall(regex, ' '.join(all_words))

for valid_word in match:
    valid_words.append(valid_word[0])

for w in all_words:
    if w in valid_words:
        pass
    else:
        invalid_words.append(w)

for barcode in all_words:
    if barcode in valid_words:
        number_char = ''
        num_numbers = 0
        barcode = re.findall(regex, ''.join(barcode))
        barcode = barcode[0][2]
        for char in barcode:
            if char.isdigit():
                num_numbers += 1
                number_char += char
            else:
                pass

        if num_numbers == 0:
            number_char = '00'

        print(f'Product group: {number_char}')

    elif barcode in invalid_words:
        print(f'Invalid barcode')
