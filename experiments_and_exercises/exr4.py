#dollars = int(input("Enter how many $ you would like to convert: "))
#rate = 0.96
#euros = dollars * rate
#print("You have " + str(euros) + " euros.")

#ranking = ['John', 'Sen', 'Mary']

#rank = int(input("Enter rank number: "))
#name = ranking[rank - 1]
#print(name)

ranking = ['John', 'Sen', 'Mary']

name = input("Enter the name: ")
rank = ranking.index(name) + 1
print(rank)