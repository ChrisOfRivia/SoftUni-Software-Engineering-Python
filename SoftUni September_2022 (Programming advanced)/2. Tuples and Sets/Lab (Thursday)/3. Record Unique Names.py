num_names = int(input())

unique_names = set()

for each_name in range(num_names):
    name = input()
    unique_names.add(name)

print("\n".join(unique_names))