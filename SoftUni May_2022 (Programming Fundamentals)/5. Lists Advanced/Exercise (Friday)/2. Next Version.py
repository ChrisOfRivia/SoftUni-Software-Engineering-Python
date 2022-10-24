version = input().split(".")

version = ''.join(version)
version = int(version)
version += 1
version = str(version)
version = '.'.join(version)
print(version)