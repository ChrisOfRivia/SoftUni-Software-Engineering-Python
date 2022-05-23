tabs_opened = int(input())
salary = int(input())

lost_salary = False

for i in range(tabs_opened):
    tabs = input()

    if tabs == "Facebook":
        salary -= 150
    elif tabs == "Instagram":
        salary -= 100
    elif tabs == "Reddit":
        salary -= 50

    if salary <= 0:
        lost_salary = True
        break


if lost_salary:
    print("You have lost your salary.")
else:
    print(salary)