kg_of_pratka = float(input())
type_usluga = input()
range_in_km = int(input())

price_km = 0
end_sum = 0
nadcenka_price = 0
express = False

if type_usluga == "standard":
    if kg_of_pratka < 1:
        price_km = 0.03
    elif 1 < kg_of_pratka <= 10:
        price_km = 0.05
    elif 10 < kg_of_pratka <= 40:
        price_km = 0.10
    elif 40 < kg_of_pratka <= 90:
        price_km = 0.15
    elif 90 < kg_of_pratka <= 150:
        price_km = 0.20


elif type_usluga == "express":
    express = True
    if kg_of_pratka < 1:
        price_km = 0.03
        nadcenka_price = kg_of_pratka * (price_km * 0.80)
    elif 1 < kg_of_pratka <= 10:
        price_km = 0.05
        nadcenka_price = kg_of_pratka * (price_km * 0.40)
    elif 10 < kg_of_pratka <= 40:
        price_km = 0.10
        nadcenka_price = kg_of_pratka * (price_km * 0.05)
    elif 40 < kg_of_pratka <= 90:
        price_km = 0.15
        nadcenka_price = kg_of_pratka * (price_km * 0.02)
    elif 90 < kg_of_pratka <= 150:
        price_km = 0.20
        nadcenka_price = kg_of_pratka * (price_km * 0.01)

if express:
    actual_price = range_in_km * price_km
    whole_nadcenka = range_in_km * nadcenka_price
    whole_sum = actual_price + whole_nadcenka
    print(f"The delivery of your "
          f"shipment with weight of {kg_of_pratka:.3f} kg. would cost {whole_sum:.2f} lv.")

else:
    end_sum = price_km * range_in_km
    print(f"The delivery of your "
          f"shipment with weight of {kg_of_pratka:.3f} kg. would cost {end_sum:.2f} lv.")