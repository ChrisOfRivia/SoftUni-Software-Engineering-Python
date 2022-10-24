import re
from time import sleep

for i in range(100):
    text = input()
    if text == '':
        break
    regex = r"\d+"

    result = re.findall(regex, text)

    for num in result:
        print(num, end=" ")