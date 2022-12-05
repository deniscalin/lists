def get_age(year_of_birth, current_year=2022):
    age = current_year - year_of_birth
    return age


birthyear = int(input("What is your year of birth? "))
age = get_age(birthyear)

if age > 120:
    print("Wow, that is amazing!")
else:
    print(age)
