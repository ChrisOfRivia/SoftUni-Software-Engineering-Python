num_pieces_already_stored = int(input())

piece_composer_key = {}

for i in range(num_pieces_already_stored):
    music1 = input()
    split1 = music1.split('|')
    piece1 = split1[0]
    composer1 = split1[1]
    key1 = split1[2]
    piece_composer_key[piece1] = [composer1]
    piece_composer_key[piece1].append(key1)

while True:
    command = input()
    if command == 'Stop':
        break
    else:
        split = command.split('|')
        action = split[0]

    if action == 'Add':
        piece = split[1]
        composer = split[2]
        key = split[3]
        if piece not in piece_composer_key.keys():
            piece_composer_key[piece] = [composer]
            piece_composer_key[piece].append(key)
            print(f'{piece} by {composer} in {key} added to the collection!')
        else:
            print(f'{piece} is already in the collection!')

    elif action == 'Remove':
        piece_remove = split[1]
        if piece_remove in piece_composer_key.keys():
            del piece_composer_key[piece_remove]
            print(f'Successfully removed {piece_remove}!')
        else:
            print(f'Invalid operation! {piece_remove} does not exist in the collection.')

    elif action == 'ChangeKey':
        piece_change_key = split[1]
        new_key = split[2]
        if piece_change_key in piece_composer_key.keys():
            piece_composer_key[piece_change_key].pop()
            piece_composer_key[piece_change_key].append(new_key)
            print(f'Changed the key of {piece_change_key} to {new_key}!')
        else:
            print(f'Invalid operation! {piece_change_key} does not exist in the collection.')

for music, writer in piece_composer_key.items():
    print(f'{music} -> Composer: {piece_composer_key[music][0]}, Key: {piece_composer_key[music][1]}')