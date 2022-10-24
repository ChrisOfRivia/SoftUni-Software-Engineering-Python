n = int(input())

for num_sentences in range(n):
    sentences = input()
    if "," in sentences or "." in sentences or "_" in sentences:
        print(f"{sentences} is not pure!")
    else:
        print(f"{sentences} is pure.")
