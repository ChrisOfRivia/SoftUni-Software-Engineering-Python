import math
from math import log

number = int(input())
base = input()
if base.isnumeric():
    base = int(base)
    result = math.log(number, base)
    print(f"{result:.2f}")
elif base == 'natural':
    result = math.log(number)
    print(f"{result:.2f}")