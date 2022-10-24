def math_operations(*args, **kwargs):
    list_floats = [float(el) for el in args]


    dict_commands = {}

    for letter, num in kwargs.items():
        dict_commands[letter] = num

    while list_floats:
        for key, value in dict_commands.items():
            if list_floats:
                if key == 'a':
                    dict_commands[key] += list_floats[0] + value
                    list_floats.pop(0)
                elif key == 's':
                    dict_commands[key] -= list_floats[0] - value
                    list_floats.pop(0)
                elif key == 'd':
                    if value == 0:
                        continue
                    else:
                        dict_commands[key] /= list_floats[0] / value
                    list_floats.pop(0)
                elif key == 'm':
                    dict_commands[key] *= list_floats[0] * value
                    list_floats.pop(0)


print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))