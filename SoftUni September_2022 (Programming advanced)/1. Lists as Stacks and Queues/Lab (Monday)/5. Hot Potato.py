from collections import deque

circle_of_kids = deque(input().split(" "))

n = int(input())
counter = 0


while len(circle_of_kids) > 1:
    circle_of_kids.rotate(-n)
    removed_kid = circle_of_kids.pop()
    print(f'Removed {removed_kid}')

print(f"Last is {''.join(circle_of_kids)}")