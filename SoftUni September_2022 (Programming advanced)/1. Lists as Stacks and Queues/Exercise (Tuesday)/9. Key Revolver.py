from collections import deque

price_of_one_bullet = int(input())
size_of_barrel = int(input())
bullets_input = input().split(' ')
locks_input = input().split(' ')
value_intelligence = int(input())
bullets = deque(bullets_input)
locks = deque(locks_input)

rounds_shooting = 0
time_reloaded = 0
bullets_used = 0

while locks and bullets:
    first_bullet = int(bullets.pop())
    first_lock = int(locks[0])

    rounds_shooting += 1
    if first_bullet > first_lock:
        print("Ping!")
        bullets_used += 1

    else:
        print("Bang!")
        locks.popleft()
        bullets_used += 1

    if rounds_shooting % size_of_barrel == 0:
        if bullets:
            print(f'Reloading!')
        time_reloaded += 1

money_used = bullets_used * price_of_one_bullet
money_used -= value_intelligence

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${abs(money_used)}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
