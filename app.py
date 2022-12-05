#from functions import write, get_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M")
print("Welcome to the Simple List Service!")
print("Time now is", now)
user_prompt = "Control your day! Add items (+), show your list (=), edit items(@), done(#) or exit: "

while True:
    # Get user input and strip any spaces from it
    user_action = input(user_prompt)
    user_action = user_action.strip()

    if user_action.startswith("add") or user_action.startswith("new"):
        todo = user_action[4:]

        todos = functions.get_todos()
        todos.append(todo + "\n")

        functions.write(todos)

        print("Added that, nice!")

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        # new_todos = [item.strip("\n") for item in todos]

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            item_no = int(user_action[5:])
            item_no = item_no - 1

            todos = functions.get_todos()

            print("OK, editing " + todos[item_no].strip("\n"))
            new_item = input("Replace " + todos[item_no].strip("\n") + " with: ")
            todos[item_no] = new_item + "\n"

            functions.write(todos)

        except ValueError:
            print("Command not valid")
            continue

    elif user_action.startswith("done"):
        try:
            item_no = int(user_action[5:])

            todos = functions.get_todos()

            completed = todos[item_no - 1].strip("\n")
            todos.pop(item_no - 1)
            print(f"{completed} is DONE! What's next?")

            functions.write(todos)

        except IndexError:
            print("No item with that number!")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Not one of the packaged commands!")

print("Have a nice day! Go get'em!")
