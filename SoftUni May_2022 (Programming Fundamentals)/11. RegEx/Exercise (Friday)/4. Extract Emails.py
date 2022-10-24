import re

regex = r'(?<=\s)(([a-z0-9]+[\-\_\.a-z0-9]*?)@[a-z\-]+(\.[a-z]+)+)\b'

emails = input()

result = re.findall(regex, emails)

for email in result:
    print(f'{email[0]}')
