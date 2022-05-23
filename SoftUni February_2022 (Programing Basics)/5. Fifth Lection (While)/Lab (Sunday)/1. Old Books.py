favourite_book = input()

book_counter = 0
book_found = False

while True:
    ask_book = input()

    if ask_book == favourite_book:
        book_found = True
        break

    if ask_book == "No More Books":
        book_found = False
        break

    book_counter += 1

if book_found:
    print(f"You checked {book_counter} books and found it.")
else:
    print(f"The book you search is not here!")
    print(f"You checked {book_counter} books.")