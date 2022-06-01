num_snowballs = int(input())

first_kid_score = 0
second_kid_score = 0

record_weight = 0
record_time = 0
record_quality = 0
highest_snowball_score = 0

for snowballs in range(1, 2 +1):
    weight_of_snowball = int(input())
    time_needed_for_snowball = int(input())
    quality_of_snowball = int(input())
    if snowballs == 1:
        first_kid_score = (weight_of_snowball / time_needed_for_snowball) ** quality_of_snowball
        record_weight = weight_of_snowball
        record_time = time_needed_for_snowball
        record_quality = quality_of_snowball
        highest_snowball_score = first_kid_score
    elif snowballs == 2:
        second_kid_score = (weight_of_snowball / time_needed_for_snowball) ** quality_of_snowball
        if second_kid_score > highest_snowball_score:
            highest_snowball_score = second_kid_score
        if second_kid_score > first_kid_score:
            record_weight = weight_of_snowball
            record_time = time_needed_for_snowball
            record_quality = quality_of_snowball
        else:
            pass
print(f'{record_weight} : {record_time} = {int(highest_snowball_score)} ({record_quality})')