capacity_of_stadium = int(input())
num_fans = int(input())

fans_in_A = 0
fans_in_B = 0
fans_in_V = 0
fans_in_G = 0

for each_fan in range(num_fans):
    sector = input()

    if sector == "A":
        fans_in_A += 1
    elif sector == "B":
        fans_in_B += 1
    elif sector == "V":
        fans_in_V += 1
    elif sector == "G":
        fans_in_G += 1

percent_A = fans_in_A / num_fans * 100
percent_B = fans_in_B / num_fans * 100
percent_V = fans_in_V / num_fans * 100
percent_G = fans_in_G / num_fans * 100

percent_fans_stadium = num_fans / capacity_of_stadium * 100

print(f"{percent_A:.2f}%")
print(f"{percent_B:.2f}%")
print(f"{percent_V:.2f}%")
print(f"{percent_G:.2f}%")
print(f"{percent_fans_stadium:.2f}%")