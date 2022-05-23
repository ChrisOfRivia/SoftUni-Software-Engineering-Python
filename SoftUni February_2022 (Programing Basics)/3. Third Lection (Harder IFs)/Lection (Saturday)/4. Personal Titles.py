age = float(input())
sex = input()

title = ""

if sex == "f":
    if age < 16:
        title = "Miss"
    else:
        title = "Ms."
if sex == "m":
    if age < 16:
        title = "Master"
    else:
        title = "Mr."

print(title)