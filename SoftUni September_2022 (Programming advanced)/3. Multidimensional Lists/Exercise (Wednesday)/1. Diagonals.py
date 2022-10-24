n = int(input())

matrix = []

primary_diag = []
secondary_diag = []

secondary_diagonal = n - 1

for i in range(n):
    matrix.append([int(el) for el in input().split(", ")])
    primary_diag.append(matrix[i][i])
    secondary_diag.append(matrix[i][secondary_diagonal])
    secondary_diagonal -= 1

print(f"Primary diagonal: {', '.join(map(str, primary_diag))}. Sum: {sum(primary_diag)}")
print(f"Secondary diagonal: {', '.join(map(str, secondary_diag))}. Sum: {sum(sec)}")




