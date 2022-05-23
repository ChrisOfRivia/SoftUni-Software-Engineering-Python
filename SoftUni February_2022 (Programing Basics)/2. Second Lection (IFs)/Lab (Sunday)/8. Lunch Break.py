from math import ceil

name_of_movie = input()
length_of_episode = int(input())
lunch_break = int(input())

time_for_lunch = lunch_break * 1/8
time_for_rest = lunch_break * 1/4

remaining_time = lunch_break - (time_for_lunch + time_for_rest)
free_time = abs(length_of_episode - remaining_time)

if remaining_time >= length_of_episode:
    print(f"You have enough time to watch {name_of_movie} "
          f"and left with {ceil(free_time)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_of_movie}, "
          f"you need {ceil(free_time)} more minutes.")