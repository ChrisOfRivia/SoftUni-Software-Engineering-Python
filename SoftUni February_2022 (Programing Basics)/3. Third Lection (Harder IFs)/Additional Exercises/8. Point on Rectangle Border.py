x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

border = False

if x == x1 or x == x2 or x == -x1 or x == -x2:
    border = True
elif y == y1 or y == y2 or y == -y1 or y == -y2:
    border = True
else:
    border = False

if border:
    print(f"Border")
else:
    print(f"Inside / Outside")