name_of_actor = input()
points_from_academy = float(input())
num_judges = int(input())

for i in range(num_judges):
    name_of_judge = input()
    points_from_judge = float(input())

    points_from_academy += (len(name_of_judge) * points_from_judge) / 2

    if points_from_academy > 1250.5:
        break

winning_points = 1250.5 + points_from_academy
diff = abs(1250.5 - points_from_academy)

if points_from_academy >= 1250.5:
    print(f"Congratulations, {name_of_actor} got"
          f" a nominee for leading role with {points_from_academy:.1f}!")
else:
    print(f"Sorry, {name_of_actor} you need {diff:.1f} more!")