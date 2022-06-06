string = input().split(" ")
shuffles = int(input())

middle_of_deck = 0
left_side_deck = []
right_side_deck = []
whole_deck = []
new_deck = whole_deck

for decks in range(shuffles):
    whole_deck = new_deck
    if decks == 0:
        for index in string:
            middle_of_deck = len(string) // 2
            if index in string[:middle_of_deck]:
                left_side_deck.append(index)
            elif index in string[middle_of_deck:]:
                right_side_deck.append(index)
        for times in range(len(left_side_deck)):
            whole_deck.append(left_side_deck[times])
            whole_deck.append(right_side_deck[times])
    else:
        left_side_deck = []
        right_side_deck = []
        new_deck = []
        for index in whole_deck:
            middle_of_deck = len(whole_deck) // 2
            if index in whole_deck[:middle_of_deck]:
                left_side_deck.append(index)
            elif index in whole_deck[middle_of_deck:]:
                right_side_deck.append(index)
        for times in range(len(left_side_deck)):
            new_deck.append(left_side_deck[times])
            new_deck.append(right_side_deck[times])
print(new_deck)