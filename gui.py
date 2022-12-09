import functions
import PySimpleGUI as sg

label = sg.Text("Control your day! Add your todo.")
inputbox = sg.InputText(tooltip="Enter todo", key="todo")
add_btn = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=(45, 10))
edit_btn = sg.Button("Edit")

window = sg.Window('Welcome to Nulist Idea Mapping Service',
                   layout=[[label], [inputbox, add_btn], [list_box, edit_btn]],
                   font=('Andale Mono', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    print(values["todos"])
    match event:
        case 'Add':
            todos = functions.get_todos()
            todos.append(values["todo"] + "\n")
            functions.write(todos)
            window["todos"].update(values=todos)

        case 'Edit':
            item_to_edit = values["todos"][0]
            new_todo = values["todo"] + "\n"

            todos = functions.get_todos()
            index = todos.index(item_to_edit)
            todos[index] = new_todo
            functions.write(todos)
            window["todos"].update(values=todos)

        case 'todos':
            clean_value = values["todos"][0].strip("\n")
            window["todo"].update(value=clean_value)

        case sg.WIN_CLOSED:
            break

window.close()
