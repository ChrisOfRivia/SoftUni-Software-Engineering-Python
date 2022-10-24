from string import ascii_lowercase

rows, cols = map(int, input().split())

alphabet = list(ascii_lowercase)

matrix = []

for i in range(rows):
    first_and_last_letter = alphabet[i]
    idx_for_letter = alphabet.index(first_and_last_letter)
    matrix.append([])
    for j in range(cols):
        matrix[i].append(first_and_last_letter+alphabet[idx_for_letter + j]+first_and_last_letter)
    print(' '.join(matrix[i]))

