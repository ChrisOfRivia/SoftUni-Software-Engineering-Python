def age_assignment(*args, **kwargs):
    result = ''
    age_dict = {}

    for names in args:
        for initials, age in kwargs.items():
            if names.startswith(initials):
                age_dict[names] = age

    sorting = dict(sorted(age_dict.items(), key=lambda x: x[0]))

    for name, age in sorting.items():
        result += f"\n{name} is {age} years old."

    return result
