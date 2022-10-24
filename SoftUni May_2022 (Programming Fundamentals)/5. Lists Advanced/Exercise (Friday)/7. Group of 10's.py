number_sequence = input().split(", ")
boundary = 0
new_list = []
fresh_list = number_sequence
while len(fresh_list) > 0:
    boundary += 10
    for num in number_sequence:
        if boundary - 10 < int(num) <= boundary:
            new_list.append(int(num))
    print(f'Group of {boundary}\'s: {new_list}')
    for nums in new_list:
        if str(nums) in number_sequence:
            fresh_list.remove(str(nums))
    new_list = []
