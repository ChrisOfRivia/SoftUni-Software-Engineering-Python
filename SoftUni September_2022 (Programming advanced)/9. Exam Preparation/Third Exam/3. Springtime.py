def start_spring(**kwargs):
    sorted_dict = {}

    for key, value in kwargs.items():
        if value not in sorted_dict:
            sorted_dict[value] = []
        sorted_dict[value].append(key)

    result = ''
    sorted_dict = dict(sorted(sorted_dict.items(), key=lambda x: (-len(x[1]), x[0])))

    for type, names in sorted_dict.items():
        result += f"{type}:\n"
        for every_name in sorted(names):
            result += f"-{every_name}\n"

    return result
