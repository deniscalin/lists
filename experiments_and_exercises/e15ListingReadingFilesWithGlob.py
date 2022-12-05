import glob
import time
#Start time
start = time.time()


myfiles = glob.glob("../files/*.txt")
for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read().upper())

        

# End time
end = time.time()
print(end - start)




# Removing the directory path from the file name
# myfiles = [filepath.strip("../files/") for filepath in myfiles]
