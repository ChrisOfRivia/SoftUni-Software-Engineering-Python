n = int(input())
word = input()

everything = []
including_word = []

for _ in range(n):
    sentences = input()
    everything.append(sentences)
    if word in sentences:
        including_word.append(sentences)
print(everything)
print(including_word)