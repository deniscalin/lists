text = "Hello"

filenames = ["document.txt", "newfile.txt", "reports.txt"]

for filename in filenames:
    file = open(f"../files/{filename}", 'w')
    file.write(text)
    file.close()