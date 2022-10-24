num_groups = int(input())

longest_intersection = []

for groups in range(num_groups):
    all_groups = input().split('-')
    first_group = all_groups[0].split(',')
    x1 = int(first_group[0])
    y1 = int(first_group[1])
    first_set = set()
    for first_numbers in range(x1, y1 + 1):
        first_set.add(first_numbers)

    second_group = all_groups[1].split(',')
    x2 = int(second_group[0])
    y2 = int(second_group[1])
    second_set = set()
    for second_numbers in range(x2, y2 + 1):
        second_set.add(second_numbers)

    if not longest_intersection:
        longest_intersection = first_set.intersection(second_set)
    else:
        if len(first_set.intersection(second_set)) > len(longest_intersection):
            longest_intersection = first_set.intersection(second_set)

longest_in_str = [str(el) for el in longest_intersection]

print(f'Longest intersection is [{", ".join(longest_in_str)}] with length {len(longest_intersection)}')