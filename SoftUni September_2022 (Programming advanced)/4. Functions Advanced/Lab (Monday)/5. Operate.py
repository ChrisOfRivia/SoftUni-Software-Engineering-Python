def operate(operator, *args, first_number=True):
    result = 0
    if operator == '+':
        for num_add in args:
            if first_number:
                result = num_add
                first_number = False
            else:
                result += num_add

        return result

    elif operator == '-':
        for num_subtract in args:
            if first_number:
                result = num_subtract
                first_number = False
            else:
                result -= num_subtract

        return result

    elif operator == '*':
        for num_times in args:
            if first_number:
                result = num_times
                first_number = False
            else:
                result *= num_times

        return result

    elif operator == '/':
        for num_divide in args:
            if first_number:
                result = num_divide
                first_number = False
            else:
                result /= num_divide

        return result

