from collections import deque

qty_of_food = int(input())

sequence_of_food_orders = input().split(' ')

deq_of_food_orders = deque()

for every_num in sequence_of_food_orders:
    deq_of_food_orders.append(int(every_num))

print(max(deq_of_food_orders))

while deq_of_food_orders:
    first_in_line = deq_of_food_orders.popleft()
    if first_in_line <= qty_of_food:
        qty_of_food -= first_in_line
    else:
        deq_of_food_orders.appendleft(first_in_line)
        break

if len(deq_of_food_orders) == 0:
    print(f"Orders complete")
else:
    new_els = [str(el) for el in deq_of_food_orders]
    print(f'Orders left: {" ".join(new_els)}')
