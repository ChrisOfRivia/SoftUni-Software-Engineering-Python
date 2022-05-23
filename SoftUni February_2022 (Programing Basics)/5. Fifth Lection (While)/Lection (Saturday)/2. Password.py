username = input()
password = input()

while True:
    guess = input()
    if guess == password:
        print(f"Welcome {username}!")
        break
    else:
        continue
