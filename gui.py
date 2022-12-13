import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("LightGrey6")

clock = sg.Text("", key="clock")
label = sg.Text("Control your day! Add your todo.")
inputbox = sg.InputText(tooltip="Enter todo", key="todo")

add_btn = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=(45, 10))
edit_btn = sg.Button("Edit")
done_btn = sg.Button("Done")
exit_btn = sg.Button("Exit")

window = sg.Window('Welcome to Nulist Idea Mapping Service',
                   layout=[[clock],
                           [label],
                           [inputbox, add_btn],
                           [list_box, edit_btn, done_btn],
                           [exit_btn]],
                   font=('Andale Mono', 20))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
#    print(event)
#    print(values)
#    print(values["todos"])
    match event:
        case 'Add':
            todos = functions.get_todos()
            todos.append(values["todo"] + "\n")
            functions.write(todos)
            window["todos"].update(values=todos)

        case 'Edit':
            try:
                item_to_edit = values["todos"][0]
                new_todo = values["todo"] + "\n"

                todos = functions.get_todos()
                index = todos.index(item_to_edit)
                todos[index] = new_todo
                functions.write(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select an item to edit.", font=("Andale Mono", 20))

        case 'todos':
            clean_value = values["todos"][0].strip("\n")
            window["todo"].update(value=clean_value)

        case 'Done':
            try:
                selected = values["todos"][0]

                todos = functions.get_todos()
                index = todos.index(selected)
                todos.pop(index)

                functions.write(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Please select an item to complete.", font=("Andale Mono", 20))

        case sg.WIN_CLOSED | 'Exit':
            break

window.close()
