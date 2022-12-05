content = ["This is a sample text. It's very basic, but good", "I want to be more honest with myself", "Ue"]

filenames = ["data.txt", "report.txt", "presentation.txt"]

for string, filename in zip(content, filenames):
    file = open(f"../files/{filename}", 'w')
    file.write(string)
    file.close()