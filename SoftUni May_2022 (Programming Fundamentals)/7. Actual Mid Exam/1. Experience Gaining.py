needed_exp = float(input())
count_of_battles = int(input())

initial_exp = 0
battles_counter = 0

for each_battle in range(count_of_battles):
    experience = float(input())
    if initial_exp >= needed_exp:
        break
    else:
        battles_counter += 1

        if battles_counter % 5 == 0:
            initial_exp -= experience * 0.10
            if initial_exp >= needed_exp:
                break
        if battles_counter % 3 == 0:
            initial_exp += experience * 0.15
            if initial_exp >= needed_exp:
                break
        if battles_counter % 15 == 0:
            initial_exp += experience * 0.05
            if initial_exp >= needed_exp:
                break
        initial_exp += experience
        if initial_exp >= needed_exp:
            break
if initial_exp >= needed_exp:
    print(f'Player successfully collected his needed experience for {battles_counter} battles.')
else:
    print(f'Player was not able to collect the needed experience, {abs(initial_exp - needed_exp):.2f} more needed.')