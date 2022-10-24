import os

directory = input()
extensions = {}

for files in os.listdir(directory):
    file = os.path.join(directory, files)
    if os.path.isfile(files):
        file_split = files.split('.')
        file_extension = "." + file_split[-1]
        if file_extension not in extensions.keys():
            extensions[file_extension] = []
        extensions[file_extension].append(files)

extensions = sorted(extensions.items(), key=lambda x: (x[0]))

with open("./text_files/4 Directory Traversal/report.txt", "w") as file:
    for extension, files in extensions:
        file.write(f"{extension}\n")
        for individual_files in sorted(files):
            file.write(f"- - - {individual_files}\n")
