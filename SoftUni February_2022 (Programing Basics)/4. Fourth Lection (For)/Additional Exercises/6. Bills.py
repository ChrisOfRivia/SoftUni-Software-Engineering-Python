months = int(input())

# water_price = 20
# internet_price = 15

percent_added = 0
electricity_bill = 0
all_bills = 0
water = 0
internet = 0
other = 0

for each_month in range(months):
    electricity_bill = float(input())

    all_bills += electricity_bill

    water = 20 * months
    internet = 15 * months

    other += (electricity_bill + 20 + 15) + ((electricity_bill + 20 + 15) * 0.20)

average = (other + water + internet + all_bills) / months

print(f"Electricity: {all_bills:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {other:.2f} lv")
print(f"Average: {average:.2f} lv")