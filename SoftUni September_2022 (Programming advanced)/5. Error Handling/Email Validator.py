class NameTooShortError(Exception):
    """Name must be more than 4 characters"""


class MustContainAtSymbolError(Exception):
    """Email must contain @"""


class InvalidDomainError(Exception):
    """Domain must be one of the following: .com, .bg, .org, .net"""


email = input()
possible_domains = ['.com', '.bg', '.org', '.net']

while email != 'End':
    if '@' in email:
        name, domain = email.split("@")
        domain = domain.split('.')
        domain = '.' + domain[1]
    else:
        raise MustContainAtSymbolError("Email must contain @")

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if domain not in possible_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print('Email is valid')
    email = input()
