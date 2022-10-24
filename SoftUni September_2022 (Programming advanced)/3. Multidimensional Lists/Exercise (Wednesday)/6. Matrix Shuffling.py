rows, cols = map(int, input().split())

matrix = []

for i in range(rows):
    matrix.append([el for el in input().split()])


while True:
    invalid = False
    command = input().split()
    if command[0] == 'END':
        break
    elif command[0] == 'swap' and len(command) == 5:
        int_of_idx = [int(el) for el in command[1::]]
        for idx, nums in enumerate(int_of_idx):
            if idx % 2 == 0:
                if nums >= rows:
                    print("Invalid input!")
                    invalid = True
                    break
                else:
                    pass

            elif idx % 2 != 0:
                if nums >= cols:
                    print("Invalid input!")
                    invalid = True
                    break
                else:
                    pass

        if not invalid:
            first_number = int_of_idx[0]
            second_number = int_of_idx[1]
            third_number = int_of_idx[2]
            fourth_number = int_of_idx[3]

            first_changing_number = matrix[first_number][second_number]
            second_changing_number = matrix[third_number][fourth_number]

            matrix[first_number][second_number] = second_changing_number
            matrix[third_number][fourth_number] = first_changing_number

            for groups in matrix:
                print(f"{' '.join(groups)}")

    else:
        print(f"Invalid input!")
