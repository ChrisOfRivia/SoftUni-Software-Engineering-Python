tickets = input().split(', ')

for ticket in tickets:
    jackpot = False
    invalid = False
    valid = False
    if ' ' in ticket:
        ticket = ticket.replace(' ', '')
    if len(ticket) == 20:
        valid = True
    else:
        invalid = True
        print(f'invalid ticket')

    if ticket.count('@') == 20:
        print(f'ticket "{ticket}" - 10@ Jackpot!')
        jackpot = True
    elif ticket.count('#') == 20:
        print(f'ticket "{ticket}" - 10# Jackpot!')
        jackpot = True
    elif ticket.count('$') == 20:
        print(f'ticket "{ticket}" - 10$ Jackpot!')
        jackpot = True
    elif ticket.count('^') == 20:
        print(f'ticket "{ticket}" - 10^ Jackpot!')
        jackpot = True

    if not jackpot:
        if ticket.count('@') >= 12:
            print(f'ticket "{ticket}" - 6@')
        elif ticket.count('#') >= 12:
            print(f'ticket "{ticket}" - 6#')
        elif ticket.count('$') >= 12:
            print(f'ticket "{ticket}" - 6$')
        elif ticket.count('^') >= 12:
            print(f'ticket "{ticket}" - 6^')

    if valid and '#' not in ticket and '@' not in ticket and '^' not in ticket and '$' not in ticket:
        print(f'ticket "{ticket}" - no match')
