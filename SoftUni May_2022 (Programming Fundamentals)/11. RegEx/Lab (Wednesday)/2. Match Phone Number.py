import re

numbers = input()

passage = r'\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b'

match = re.findall(passage, numbers)

print(', '.join(match))
