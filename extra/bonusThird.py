brand_names = ['ryoto', 'MayNight', 'Wondero']

while True:
    user_input = input("Type begin to get this started: ")
    match user_input:
        case 'begin':
            for brand in brand_names:
                print(brand.upper())
            break
        case _:
            print("Sorry, it has to be begin :)")

print("You did good!")
