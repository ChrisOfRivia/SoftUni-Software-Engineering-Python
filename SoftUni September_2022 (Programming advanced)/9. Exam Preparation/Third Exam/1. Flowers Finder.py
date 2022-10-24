from collections import deque

flowers = ['rose', 'tulip', 'lotus', 'daffodil']

flowers_chr = [['r', 'o', 's', 'e'], ['t', 'u', 'l', 'i', 'p'], ['l', 'o', 't', 'u', 's'],
               ['d', 'a', 'ff', 'o', 'd', 'i', 'l']]

words = {'rose': ['', '', '', ''], 'tulip': ['', '', '', '', ''],
         'lotus': ['', '', '', '', ''], 'daffodil': ['', '', '', '', '', '', '']}

found_word = ''
word_found = False

vowels = deque(input().split())
consonants = deque(input().split())

while vowels and consonants:
    if word_found:
        break

    first_vowel = vowels.popleft()
    last_consonant = consonants.pop()
    if last_consonant == 'f':
        last_consonant = 'ff'

    for every_flower in flowers_chr:
        if first_vowel in every_flower:
            idx = every_flower.index(first_vowel)
            words["".join(every_flower)][idx] = first_vowel

    for every_flower in flowers_chr:
        if last_consonant in every_flower:
            if last_consonant == 'd':
                words["".join(every_flower)][every_flower.index(last_consonant)] = last_consonant
                words["".join(every_flower)][4] = last_consonant

            else:
                words["".join(every_flower)][every_flower.index(last_consonant)] = last_consonant

    for letters in words.values():
        if ''.join(letters) in flowers:
            found_word = ''.join(letters)
            word_found = True
            break

if found_word:
    print(f'Word found: {found_word}')
else:
    print(f'Cannot find any word!')

if vowels:
    print(f'Vowels left: {" ".join(vowels)}')

if consonants:
    print(f'Consonants left: {" ".join(consonants)}')
