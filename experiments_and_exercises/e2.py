print("Welcome to Simple To Do List Service!")
user_prompt = "Items to do in the next hour: "
user_todos_list = []

while True:
    todo_item = input(user_prompt)
    title = todo_item.title()
    print(title)
    user_todos_list.append(title)
    print(user_todos_list)
