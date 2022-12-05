from extra.bonus12converter import convert
from extra.bonus12parser import parse

feet_inches = input("Enter feet and inches here (e.g. 5 11): ")

parsed = parse(feet_inches)
meters = convert(parsed['feet'], parsed['inches'])
print(f"You entered {parsed['feet']} feet and {parsed['inches']} inches, that is {meters} meters!")

if meters < 1:
    print("Not tall enough to ride. Maybe next year!")
else:
    print("OK, come on in!")



