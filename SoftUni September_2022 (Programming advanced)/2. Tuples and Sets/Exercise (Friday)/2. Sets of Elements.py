n_m = input().split(' ')
n = int(n_m[0])
m = int(n_m[1])

n_set = set()
m_set = set()

for i in range(n):
    n_numbers = int(input())
    n_set.add(n_numbers)

for j in range(m):
    m_numbers = int(input())
    m_set.add(m_numbers)

repeated_elements = n_set.intersection(m_set)

for repeated_nums in repeated_elements:
    print(repeated_nums)