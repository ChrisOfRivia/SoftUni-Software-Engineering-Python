hours = int(input())
minutes = int(input()) + 15

total_time = (hours * 60 + minutes)

current_minutes = total_time % 60
current_minutes_hour = total_time // 60


if current_minutes_hour > 23:
    print(f"0:{current_minutes:02d}")
else:
    print(f"{current_minutes_hour}:{current_minutes:02d}")



