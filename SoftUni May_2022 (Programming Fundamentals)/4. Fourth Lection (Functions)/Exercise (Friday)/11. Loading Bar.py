def loading_bar(bar_value):
    if bar_value == 100:
        return f'100% Complete! \n' \
               f'[%%%%%%%%%%]'
    else:
        return f'{bar_value}% ' \
               f'[{(bar_value // 10) * "%"}{"." * abs(10 - bar_value // 10)}] \n' \
               f'Still loading...'


bar_number = int(input())
print(loading_bar(bar_number))