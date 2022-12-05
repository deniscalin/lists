def count_names(names_local):
    parsed = names.split(",")
    number_local = len(parsed)
    return number_local


names = input("Enter names separated by commas (no spaces): ")
number = count_names(names)
print(number)
