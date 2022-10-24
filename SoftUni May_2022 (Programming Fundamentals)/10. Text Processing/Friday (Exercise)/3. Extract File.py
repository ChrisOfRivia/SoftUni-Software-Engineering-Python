file = input().split("\\")

file_location = file[-1]

file_name, file_extension = file_location.split('.')

print(f'File name: {file_name}')
print(f'File extension: {file_extension}')