goal = 10000

sum_steps = 0

while True:
    steps = input()

    if steps == "Going home":
        steps_home = int(input())
        sum_steps += steps_home
        break

    sum_steps += int(steps)
    if sum_steps >= goal:
        break

diff = abs(sum_steps - goal)

if sum_steps >= goal:
    print(f"Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")