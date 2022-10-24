import re

text_string = input()

regex = r'((?P<sep>@|#)(?P<word>[A-Za-z]{3,})(?P=sep)(?P=sep)(?P<second_word>[A-Za-z]{3,}))(?P=sep)'

match = [items.groupdict() for items in re.finditer(regex, text_string)]

all_dict_words = {}
mirror_words = {}
other_words = {}

no_mirror = False
no_pair = False

list_mirror_words = []

for group in match:
    if group['word'] == group['second_word'][::-1]:
        mirror_words[group['word']] = group['second_word']
    else:
        other_words[group['word']] = group['second_word']

    all_dict_words[group['word']] = group['second_word']


if len(all_dict_words) != 0:
    print(f'{len(all_dict_words)} word pairs found!')
else:
    print(f'No word pairs found!')

if len(mirror_words) != 0:
    print(f'The mirror words are:')
    for key, value in mirror_words.items():
        list_mirror_words.append(f'{key} <=> {value}')
    print(', '.join(list_mirror_words))
else:
    print(f'No mirror words!')