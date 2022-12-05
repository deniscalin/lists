def convert(liters_local):
    meters3 = float(liters_local) / 1000
    return meters3


liters = input("Enter amount of liters to convert: ")
print(convert(liters))
