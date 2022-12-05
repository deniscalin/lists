user_country = input("Let us know which country you're from: ")
user_country = user_country.capitalize()

match user_country:
    case 'USA' | 'Usa':
        print('Hello')
    case 'India':
        print('Namaste')
    case 'Germany':
        print('Hallo')