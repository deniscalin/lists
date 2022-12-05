list = ["a", "b", "c"]

for textfile in list:
    file = open(f"/Users/deniscalin/Downloads/{textfile}.txt", 'r')
    content = file.read()
    print(content)