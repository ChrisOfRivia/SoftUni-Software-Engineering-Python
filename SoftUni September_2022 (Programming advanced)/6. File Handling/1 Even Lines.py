from collections import deque

list_to_append = deque()

with open("text_files/1 Original_text/text.txt", "r") as file:
    whole_text = file.read()
    sentences = whole_text.split('\n')
    for idx, line in enumerate(sentences):
        if idx % 2 == 0:
            list_words = line.split(' ')
            for each_word in list_words:
                each_word = each_word.replace('-', '@')
                each_word = each_word.replace(',', '@')
                each_word = each_word.replace('.', '@')
                each_word = each_word.replace('!', '@')
                each_word = each_word.replace('?', '@')

                list_to_append.appendleft(each_word)
        print(' '.join(list_to_append))
        list_to_append.clear()
