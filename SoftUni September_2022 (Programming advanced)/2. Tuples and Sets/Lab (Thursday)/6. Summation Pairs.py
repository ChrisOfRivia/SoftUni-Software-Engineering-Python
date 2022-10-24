numbers = set(map(int, input().split(" ")))
sum_num = int(input())

used_nums = set()

for first_num in numbers:
    for second_num in numbers:
        if first_num + second_num == sum_num:
            if first_num not in used_nums and second_num not in used_nums:
                print(f'{first_num} + {second_num} = {sum_num}')
                used_nums.add(first_num)
                used_nums.add(second_num)

