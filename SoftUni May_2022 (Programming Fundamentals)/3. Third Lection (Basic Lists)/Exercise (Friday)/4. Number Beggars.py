string_of_int = input().split(", ")
count_of_beggars = int(input())

end = False
offer = 0
money_offers = []
offers_for_each_beggar = []
end_offers_for_each = []


for index in string_of_int:
    money_offers.append(int(index))

for beggars in range(count_of_beggars):
    while beggars < count_of_beggars:
        offers_for_each_beggar.append(money_offers[beggars::count_of_beggars])
        for i in offers_for_each_beggar[beggars]:
            offer += i
        end_offers_for_each.append(offer)
        offer = 0
        beggars += 1
        if beggars + 1 > count_of_beggars:
            end = True
    if end:
        break
print(end_offers_for_each)