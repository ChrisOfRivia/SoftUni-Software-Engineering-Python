head_smash_keyboard = input().upper()
unique_symbols = ''
current_symbol = ''
repetitions = ''

for index in range(len(head_smash_keyboard)):
    if not head_smash_keyboard[index].isdigit():
        current_symbol += head_smash_keyboard[index]
    else:
        for check_next_symbols in range(index, len(head_smash_keyboard)):
            if not head_smash_keyboard[check_next_symbols].isdigit():
                break
            repetitions += head_smash_keyboard[check_next_symbols]
        repetitions = int(repetitions)
        unique_symbols += repetitions * current_symbol
        current_symbol = ''
        repetitions = ''

print(f'Unique symbols used: {len(set(unique_symbols))}')
print(unique_symbols)
