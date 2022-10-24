import re

names = input()

passage = r"\b([A-Z][a-z]+ [A-Z][a-z]+)\b"

matches = re.findall(passage, names)

print(' '.join(matches))
