def data_types(data, num):
    if data == 'int':
        num = int(num)
        return num * 2
    elif data == 'real':
        num = float(num)
        return f'{num * 1.5:.2f}'
    elif data == 'string':
        return f'${num}$'


data_type_input = input()
convertable_num = input()
print(data_types(data_type_input, convertable_num))
