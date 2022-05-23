city = input()
volume_of_sales = float(input())

commission = 0
condition = False

if city not in "Sofia, Varna Plovdiv:" or volume_of_sales < 0:
    condition = True


if city == "Sofia":
    if 0 <= volume_of_sales <= 500:
        commission = 0.05
    elif 500 < volume_of_sales <= 1000:
        commission = 0.07
    elif 1000 < volume_of_sales <= 10000:
        commission = 0.08
    elif volume_of_sales > 10000:
        commission = 0.12
elif city == "Varna":
    if 0 <= volume_of_sales <= 500:
        commission = 0.045
    elif 500 < volume_of_sales <= 1000:
        commission = 0.075
    elif 1000 < volume_of_sales <= 10000:
        commission = 0.10
    elif volume_of_sales > 10000:
        commission = 0.13
elif city == "Plovdiv":
    if 0 <= volume_of_sales <= 500:
        commission = 0.055
    elif 500 < volume_of_sales <= 1000:
        commission = 0.08
    elif 1000 < volume_of_sales <= 10000:
        commission = 0.12
    elif volume_of_sales > 10000:
        commission = 0.145

diff = volume_of_sales * commission

if condition:
    print("error")
else:
    print(f"{diff:.2f}")