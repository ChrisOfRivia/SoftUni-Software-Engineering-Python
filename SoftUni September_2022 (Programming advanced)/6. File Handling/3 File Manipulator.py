import os
from os import path
from os import remove

output_folder_path = 'text_files/3 File Manipulator text files/'

while True:
    command = input().split('-')
    if command[0] == 'End':
        break

    elif command[0] == 'Create':
        file_name_create = command[1]
        if not path.exists(f"{output_folder_path}{file_name_create}"):
            open(f"{output_folder_path}{file_name_create}", 'x')
        else:
            os.remove(f"{output_folder_path}{file_name_create}")
            open(f"{output_folder_path}{file_name_create}", 'x')

    elif command[0] == 'Add':
        file_name_add = command[1]
        content_add = command[2]
        with open(f"{output_folder_path}{file_name_add}", 'a') as file_add:
            file_add.write(f"{content_add}\n")

    elif command[0] == 'Replace':
        file_name_replace = command[1]
        old_str = command[2]
        new_str = command[3]
        if path.exists(f"{output_folder_path}{file_name_replace}"):
            with open(f"{output_folder_path}{file_name_replace}", 'r+') as file_replace:
                whole_text = file_replace.read()
                whole_text = whole_text.replace(old_str, new_str)

                file_replace.close()
                with open(f"{output_folder_path}{file_name_replace}", 'r+') as file_replace:
                    file_replace.write(whole_text)
        else:
            print('An error occurred')

    elif command[0] == 'Delete':
        file_name_delete = command[1]
        if path.exists(f"{output_folder_path}{file_name_delete}"):
            remove(f"{output_folder_path}{file_name_delete}")
        else:
            print('An error occurred')
