num_orders = int(input())
all_prices = 0

# •	Price per capsule - a floating-point number in the range [0.01…100.00]
# •	Days - integer in the range [1…31]
# •	Capsules, needed per day - integer in the range [1…2000]


for orders in range(num_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100.00 or days < 1 or days > 31 or capsules_per_day < 1 or capsules_per_day > 2000:
        continue
    price = price_per_capsule * days * capsules_per_day
    all_prices += price
    print(f"The price for the coffee is: ${price:.2f}")
print(f"Total: ${all_prices:.2f}")