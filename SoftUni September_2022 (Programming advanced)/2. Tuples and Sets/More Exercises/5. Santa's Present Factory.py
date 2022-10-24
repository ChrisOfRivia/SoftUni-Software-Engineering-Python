from collections import deque

mats_for_toys = list(map(int, input().split(" ")))
magic_level = deque(map(int, input().split(" ")))

crafted_toys = {}
crafted_toys['Doll'] = [0]
crafted_toys['Wooden train'] = [0]
crafted_toys['Teddy bear'] = [0]
crafted_toys['Bicycle'] = [0]

while mats_for_toys and magic_level:
    last_mat_box = mats_for_toys[-1]
    first_magic_lvl = magic_level[0]
    result = last_mat_box * first_magic_lvl

    if result == 150:
        mats_for_toys.pop()
        magic_level.popleft()
        crafted_toys['Doll'][0] += 1
    elif result == 250:
        mats_for_toys.pop()
        magic_level.popleft()
        crafted_toys['Wooden train'][0] += 1
    elif result == 300:
        mats_for_toys.pop()
        magic_level.popleft()
        crafted_toys['Teddy bear'][0] += 1
    elif result == 400:
        mats_for_toys.pop()
        magic_level.popleft()
        crafted_toys['Bicycle'][0] += 1
    elif result < 0:
        new_sum = abs(last_mat_box + first_magic_lvl)
        mats_for_toys.pop()
        magic_level.popleft()
        mats_for_toys.append(new_sum)
    elif result > 0:
        magic_level.popleft()
        mats_for_toys[-1] += 15
    elif result == 0:
        if last_mat_box == 0:
            mats_for_toys.pop()
        if first_magic_lvl == 0:
            magic_level.popleft()
        continue

if crafted_toys['Doll'][0] > 0 and crafted_toys['Wooden train'][0] > 0 or crafted_toys['Teddy bear'][0] > 0 and crafted_toys['Bicycle'][0] > 0:
    print(f'The presents are crafted! Merry Christmas!')
else:
    print(f"No presents this Christmas!")

if mats_for_toys:
    print(f'Materials left: {", ".join(map(str, reversed(mats_for_toys)))}')
if magic_level:
    print(f'Magic left: {", ".join(map(str, magic_level))}')

for_order_of_presents = []
for present, qty in crafted_toys.items():
    if qty[0] != 0:
        for_order_of_presents.append(f"{present}: {qty[0]}")

for_order_of_presents = sorted(for_order_of_presents)

for presents in for_order_of_presents:
    print(presents)

