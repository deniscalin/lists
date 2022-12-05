def get_max():
    grades = [9.6, 9.2, 9.7]
    max_number = max(grades)
    min_number = min(grades)
    message = f"Max: {max_number}, Min: {min_number}"
    return message


print(get_max())
