vacation_days = int(input())

diff_free_days = 365 - vacation_days

play_during_work_day = diff_free_days * 63
play_during_free_day = vacation_days * 127

all_year = play_during_work_day + play_during_free_day

diff = abs(30000 - all_year)

turn_into_minutes = diff % 60
turn_into_hours = diff // 60

if all_year >= 30000:
    print(f"Tom will run away")
    print(f"{turn_into_hours} hours and {turn_into_minutes} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{turn_into_hours} hours and {turn_into_minutes} minutes less for play")

