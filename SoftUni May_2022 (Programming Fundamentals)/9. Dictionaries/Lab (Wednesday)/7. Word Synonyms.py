synonyms = {}

n = int(input())

for times in range(n):
    key = input()
    synonym = input()

    if key not in synonyms:
        synonyms[key] = []
    synonyms[key].append(synonym)

for key, value in synonyms.items():
    print(f'{key} - {", ".join(value)}')
