from collections import deque

eggs = deque(map(int, input().split(', ')))
pieces_of_paper = list(map(int, input().split(', ')))

wrapped_eggs = []

while eggs and pieces_of_paper:
    first_egg = eggs[0]
    if first_egg <= 0:
        eggs.popleft()
        continue
    elif first_egg == 13:
        eggs.popleft()
        first_paper = pieces_of_paper[0]
        last_paper = pieces_of_paper[-1]

        pieces_of_paper[0] = last_paper
        pieces_of_paper[-1] = first_paper
        continue

    last_piece_of_paper = pieces_of_paper[-1]

    if first_egg + last_piece_of_paper <= 50:
        wrapped_eggs.append(first_egg + last_piece_of_paper)
        eggs.popleft()
        pieces_of_paper.pop()
    else:
        eggs.popleft()
        pieces_of_paper.pop()

if wrapped_eggs:
    print(f"Great! You filled {len(wrapped_eggs)} boxes.")
else:
    print(f"Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join(map(str, eggs))}")

if pieces_of_paper:
    print(f"Pieces of paper left: {', '.join(map(str, pieces_of_paper))}")




