password = input("Check your password here: ")


def checker(password_local):
    checks = {}

    long = False
    if len(password_local) >= 8:
        checks["is_long"] = True
    else:
        checks["is_long"] = False

    has_upper = False
    for i in password_local:
        if i.isupper():
            has_upper = True

    checks["has_upper"] = has_upper

    has_digit = False
    for i in password_local:
        if i.isdigit():
            has_digit = True

    checks["has_digit"] = has_digit

    print(checks)

    if all(checks.values()):
        result = "Strong password!"
    else:
        result = "Weak password"

    return result


print(checker(password))

