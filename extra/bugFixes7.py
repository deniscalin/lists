temperatures = [10, 12, 14]
temperatures = [str(item) + "\n" for item in temperatures]

file = open("file.txt", 'w')

file.writelines(temperatures)