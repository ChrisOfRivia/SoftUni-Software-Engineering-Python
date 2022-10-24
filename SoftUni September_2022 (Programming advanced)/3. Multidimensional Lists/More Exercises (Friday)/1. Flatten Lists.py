matrix = input().split("|")

actual_matrix = []

for i in matrix[::-1]:
    actual_matrix.extend(i.split())

print(' '.join(actual_matrix))

