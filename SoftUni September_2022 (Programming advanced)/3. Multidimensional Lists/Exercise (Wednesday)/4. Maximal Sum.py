rows, cols = map(int, input().split())

rectangle = []
max_sum = [0]

for row in range(rows):
    rectangle.append([int(el) for el in input().split()])

for i in range(rows - 2):
    for j in range(cols - 2):
        if rectangle[i][j] + rectangle[i][j + 1] + rectangle[i][j + 2] + rectangle[i + 1][j] + rectangle[i + 1][j + 1] + rectangle[i + 1][j + 2] + rectangle[i + 2][j] + rectangle[i + 2][j + 1] + rectangle[i + 2][j + 2] > sum(max_sum):
            max_sum = [rectangle[i][j], rectangle[i][j + 1], rectangle[i][j + 2], rectangle[i + 1][j], rectangle[i + 1][j + 1], rectangle[i + 1][j + 2], rectangle[i + 2][j], rectangle[i + 2][j + 1], rectangle[i + 2][j + 2]]

print(f"Sum = {sum(max_sum)}")
print(max_sum[0], max_sum[1], max_sum[2])
print(max_sum[3], max_sum[4], max_sum[5])
print(max_sum[6], max_sum[7], max_sum[8])