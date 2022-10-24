first_words = input().split(", ")
second_words = input().split(", ")
repetitive_words = []

for first in first_words:
    for second in second_words:
        if first in second:
            repetitive_words.append(first)
            break
print(repetitive_words)