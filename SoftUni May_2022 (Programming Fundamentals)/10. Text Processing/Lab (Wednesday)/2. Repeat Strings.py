words = input().split(" ")

comprehension = [word * len(word) for word in words]

print(''.join(comprehension))