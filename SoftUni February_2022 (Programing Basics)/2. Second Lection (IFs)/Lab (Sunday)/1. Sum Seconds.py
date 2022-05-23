first_runner = int(input())
second_runner = int(input())
third_runner = int(input())

all_seconds = first_runner + second_runner + third_runner

minutes = all_seconds // 60
seconds = all_seconds % 60

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")

