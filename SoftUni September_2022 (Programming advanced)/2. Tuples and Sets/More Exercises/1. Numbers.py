first_sequence = {*input().split(" ")}
second_sequence = {*input().split(" ")}

n = int(input())

for i in range(n):
    command = input().split(" ")

    numbers = [el for el in command if el.isdigit()]

    if command[0] == 'Add' and command[1] == 'First':
        for num in numbers:
            first_sequence.add(num)
    elif command[0] == 'Add' and command[1] == 'Second':
        for num in numbers:
            second_sequence.add(num)
    elif command[0] == 'Remove' and command[1] == 'First':
        for num in numbers:
            if num in first_sequence:
                first_sequence.remove(num)
    elif command[0] == 'Remove' and command[1] == 'Second':
        for num in numbers:
            if num in second_sequence:
                second_sequence.remove(num)
    elif command[0] == 'Check' and command[1] == 'Subset':
        if first_sequence.issubset(second_sequence):
            print('True')
        elif second_sequence.issubset(first_sequence):
            print("True")
        else:
            print("False")

print(', '.join(map(str, sorted(map(int, first_sequence)))))
print(', '.join(map(str, sorted(map(int, second_sequence)))))
