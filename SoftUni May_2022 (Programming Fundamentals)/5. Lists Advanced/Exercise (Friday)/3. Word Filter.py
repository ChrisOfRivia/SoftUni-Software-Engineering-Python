words_list = input().split()

filtered_words = [words for words in words_list if len(words) % 2 == 0]

print('\n'.join(filtered_words))