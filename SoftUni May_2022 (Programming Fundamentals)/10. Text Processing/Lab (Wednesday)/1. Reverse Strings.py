def reverse_func(word):
    return f'{word} = {word[::-1]}'


while True:
    random_word = input()
    if random_word == 'end':
        break
    print(reverse_func(random_word))
