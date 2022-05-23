season = input()
type_group = input()
num_students = int(input())
num_sleepovers = int(input())

price = 0
type_training = ""

if season == "Winter":
    if type_group in "boys, girls":
        price = 9.60
        if type_group == "girls":
            type_training = "Gymnastics"
        elif type_group == "boys":
            type_training = "Judo"
    elif type_group == "mixed":
        type_training = "Ski"
        price = 10

elif season == "Spring":
    if type_group in "boys, girls":
        price = 7.20
        if type_group == "girls":
            type_training = "Athletics"
        elif type_group == "boys":
            type_training = "Tennis"
    elif type_group == "mixed":
        type_training = "Cycling"
        price = 9.50
elif season == "Summer":
    if type_group in "boys, girls":
        price = 15
        if type_group == "girls":
            type_training = "Volleyball"
        elif type_group == "boys":
            type_training = "Football"
    elif type_group == "mixed":
        type_training = "Swimming"
        price = 20

whole_price = num_sleepovers * price * num_students

if num_students >= 50:
    whole_price -= whole_price * 0.50
elif 20 <= num_students < 50:
    whole_price -= whole_price * 0.15
elif 10 <= num_students < 20:
    whole_price -= whole_price * 0.05

print(f"{type_training} {whole_price:.2f} lv.")
