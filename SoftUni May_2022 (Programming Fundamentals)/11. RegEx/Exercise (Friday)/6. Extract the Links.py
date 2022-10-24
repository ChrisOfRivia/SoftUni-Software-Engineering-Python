import re

regex = r'(www\.[A-Za-z0-9\-]*)([\.a-z]+)+'

while True:
    text = input()
    if text:
        pass
    else:
        break

    matches = re.findall(regex, text)
    if matches and len(matches[0][1]) > 1:
        print(f'{matches[0][0]}{matches[0][1]}')
