deposit_value = float(input())
srok_of_deposit = int(input())
annual_lihven_procent = float(input())

natural_lihva = deposit_value * (annual_lihven_procent / 100)
lihva_for_month = natural_lihva / 12
whole_sum = deposit_value + (srok_of_deposit * lihva_for_month)

print(whole_sum)

