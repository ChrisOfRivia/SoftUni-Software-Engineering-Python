def rectangle(length, width):
    if width != str(width) and length != str(length):
        area = length * width
        perimeter = 2 * length + 2 * width
        result = f'Rectangle area: {area}'
        result += f'\nRectangle perimeter: {perimeter}'

        return result

    else:
        return f'Enter valid values!'


print(rectangle(2, 10))