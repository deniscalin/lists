date = input("Enter today's date: ")
mood = input("On the scale of 1-10, enter is your mood: ")
thoughts = input("Let your thoughts flow: ")

with open(f"../journal/{date}.txt", "w") as file:
    file.write(mood + 2 * "\n")
    file.write(thoughts)

print("Thank you! We got your input!")
