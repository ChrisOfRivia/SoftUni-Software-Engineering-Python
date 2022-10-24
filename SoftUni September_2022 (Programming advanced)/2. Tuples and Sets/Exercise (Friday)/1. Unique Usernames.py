num_names = int(input())

unique_names = set()

for names in range(num_names):
    new_name = input()
    unique_names.add(new_name)

for unique in unique_names:
    print(unique)