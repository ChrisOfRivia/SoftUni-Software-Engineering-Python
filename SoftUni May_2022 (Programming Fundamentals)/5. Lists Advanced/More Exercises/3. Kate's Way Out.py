separated_symbols = []
maze_map = []

rows_of_maze = int(input())

for maze in range(rows_of_maze):
    pattern = input()
    separated_symbols = []
    for symbols in pattern:
        separated_symbols.append(symbols)
    maze_map.append(separated_symbols)

for each_row in maze_map:
    for index, each_symbol in enumerate(each_row):
        if each_symbol == 'k':
            if each_row[index - 1] == ' ':
                each_row[index - 1], each_row[index] = 'k', '#'


# [#, #, #, #, #, #]
# [#, #, ', ', k, #]
# [#, #, ', #, #, #]
# [#, #, ', #, #, #]
