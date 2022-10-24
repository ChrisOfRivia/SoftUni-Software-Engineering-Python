from string import punctuation

line_counter = 0

output_path = 'text_files/2 Even Lines output/line_numbers'

with open('text_files/1 Original_text/text.txt', 'r') as file1:
    text = file1.read()
    sentences = text.split("\n")
    for line in sentences:
        if not line:
            break

        letters = 0
        punctuation_marks = 0
        line_counter += 1

        for ch in line:
            if ch in punctuation:
                punctuation_marks += 1
            elif ch.isalpha():
                letters += 1

        with open(output_path, 'a') as file2:
            file2.write(f"Line {line_counter}: {line} ({letters})({punctuation_marks})\n")
