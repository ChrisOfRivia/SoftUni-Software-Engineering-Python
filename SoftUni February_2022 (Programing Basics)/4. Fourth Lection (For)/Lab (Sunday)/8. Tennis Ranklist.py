# W = 2000
# F = 1200
# SF = 720
from math import floor

points = 0
wins = 0

number_tournaments = int(input())
starting_points = int(input())

for i in range(number_tournaments):
    ranking = input()

    if ranking == "W":
        points += 2000
        wins += 1
    elif ranking == "F":
        points += 1200
    elif ranking == "SF":
        points += 720

all_points = starting_points + points
average_points = points / number_tournaments
percent_wins = (wins / number_tournaments) * 100

print(f"Final points: {floor(all_points)}")
print(f"Average points: {floor(average_points)}")
print(f"{percent_wins:.2f}%")