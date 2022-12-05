print("Welcome to Simple To Do List Service!")
user_prompt = "Enter add, show, SHOW or exit: "
todos = []

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input('Enter item: ')
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'SHOW':
            for item in todos:
                item = item.upper()
                print(item)
        case 'exit':
            break

print("Have a nice day! Go get'em!")