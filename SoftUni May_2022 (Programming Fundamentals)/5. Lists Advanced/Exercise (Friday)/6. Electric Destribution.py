num_electrons = int(input())
shell = [0]
shell_position = 0

while num_electrons > 0:
    shell_position += 1
    if num_electrons > shell[0] == 0:
        shell[0] += num_electrons
    if shell[shell_position - 1] > 2 * shell_position ** 2:
        shell[shell_position -1] = 2 * shell_position ** 2
        num_electrons -= shell[shell_position - 1]
        shell.append(num_electrons)
    else:
        break

print(shell)