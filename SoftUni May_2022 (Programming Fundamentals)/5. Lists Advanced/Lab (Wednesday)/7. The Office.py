happiness_score = list(map(int, input().split(" ")))
factor = int(input())
multiplied_nums = []
all_nums = 0
num_counter = 0
happy_counter = 0

for every_num in happiness_score:
    every_num *= factor
    num_counter += 1
    all_nums += every_num
    multiplied_nums.append(every_num)

average_nums = all_nums / num_counter

for num in multiplied_nums:
    if num >= average_nums:
        happy_counter += 1

if happy_counter >= len(happiness_score) // 2:
    print(f'Score: {happy_counter}/{len(happiness_score)}. Employees are happy!')
else:
    print(f'Score: {happy_counter}/{len(happiness_score)}. Employees are not happy!')
