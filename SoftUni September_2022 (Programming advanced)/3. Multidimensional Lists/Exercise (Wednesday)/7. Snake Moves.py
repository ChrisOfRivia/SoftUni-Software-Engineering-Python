from collections import deque

rows, cols = map(int, input().split(" "))

word = input()

matrix = []

rest_of_word = ''
counter = 0

for i in range(rows):
    matrix.append(deque())
    rest_of_word = ''
    while len(matrix[i]) < cols:
        for ch in word:
            if len(matrix[i]) == cols:
                rest_of_word += ch
                if counter == len(word):
                    word = rest_of_word + word[counter % len(word)]
                    break

            elif i % 2 == 0:
                matrix[i].append(ch)
            else:
                matrix[i].appendleft(ch)
            counter += 1

for groups in matrix:
    print(''.join(groups))
