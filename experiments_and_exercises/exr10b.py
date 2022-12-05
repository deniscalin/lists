waiting_list = ["john", "marry"]
try:
    name = input("Enter name: ")
    number = waiting_list.index(name)
    print(f"{name}'s turn is {number + 1}")
except ValueError:
    print(f"{name} is not in the list.")