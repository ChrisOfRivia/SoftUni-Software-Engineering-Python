def math_operations(str_num_sign_num):
    first_num, sign, second_num = str_num_sign_num.split()
    first_num = float(first_num)
    second_num = int(second_num)

    result = 0
    if sign == '/':
        result = first_num / second_num

    elif sign == '*':
        result = first_num * second_num

    elif sign == '-':
        result = first_num - second_num

    elif sign == '+':
        result = first_num + second_num

    elif sign == '^':
        result = first_num ** second_num

    return f"{result:.2f}"
