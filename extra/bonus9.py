password = input("Enter your password to check: ")
result = {}

if len(password) >= 8:
    result["long"] = True
else:
    result["long"] = False


digit = False
for item in password:
    if item.isdigit():
        digit = True

result["has_digit"] = digit


upper = False
for item in password:
    if item.isupper():
        upper = True

result["has_upper"] = upper
print(result)

if all(result.values()):
    print("Good! This is a strong password!")
else:
    print("Create a stronger password.")

#if result.count(False) == 0:
#    print(result)
#    print("Strong password!")
#else:
#    print("Work on your password")