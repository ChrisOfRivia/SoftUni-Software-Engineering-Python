n = int(input())

all_people = 0
musala_trekking = 0
monblan_trekking = 0
kilimanjaro_trekking = 0
k2_trekking = 0
everest_trekking = 0

for i in range(n):
    number_people = int(input())
    all_people += number_people

    if 0 < number_people <= 5:
        musala_trekking += number_people
    elif 6 <= number_people <= 12:
        monblan_trekking += number_people
    elif 13 <= number_people <= 25:
        kilimanjaro_trekking += number_people
    elif 26 <= number_people <= 40:
        k2_trekking += number_people
    elif number_people >= 41:
        everest_trekking += number_people

percent_musala = (musala_trekking / all_people) * 100
percent_monblan = (monblan_trekking / all_people) * 100
percent_kilimanjaro = (kilimanjaro_trekking / all_people) * 100
percent_k2 = (k2_trekking / all_people) * 100
percent_everest = (everest_trekking / all_people) * 100

print(f"{percent_musala:.2f}%")
print(f"{percent_monblan:.2f}%")
print(f"{percent_kilimanjaro:.2f}%")
print(f"{percent_k2:.2f}%")
print(f"{percent_everest:.2f}%")