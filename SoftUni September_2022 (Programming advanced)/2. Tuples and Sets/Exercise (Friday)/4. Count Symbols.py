characters = {}
text = input()

for ch in text:
    if ch not in characters:
        characters[ch] = 0
    characters[ch] += 1

sorted_characters = sorted(characters)

for sorted_ch in sorted_characters:
    print(f'{sorted_ch}: {characters[sorted_ch]} time/s')
