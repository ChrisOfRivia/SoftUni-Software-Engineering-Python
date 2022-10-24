num_elements = int(input())

unique_elements = set()

for elements in range(num_elements):
    new_elements = input().split(" ")
    for each_el in new_elements:
        unique_elements.add(each_el)

print("\n".join(unique_elements))