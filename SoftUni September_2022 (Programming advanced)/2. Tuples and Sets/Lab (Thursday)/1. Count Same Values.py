numbers = tuple((map(float, input().split(' '))))

empty_list = []

for each_num in numbers:
    if each_num not in empty_list:
        print(f'{each_num} - {numbers.count(each_num)} times')
        empty_list.append(each_num)
