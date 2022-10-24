numbers = input().split(' ')

stack_nums = []

while numbers:
    reversed_num = numbers.pop()
    stack_nums.append(reversed_num)

print(' '.join(stack_nums))
