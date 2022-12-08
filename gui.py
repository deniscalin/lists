import functions
import PySimpleGUI as sg

label = sg.Text("Control your day! Add your todo.")
inputbox = sg.InputText(tooltip="Enter todo", key="todo")
add_btn = sg.Button("Add")

window = sg.Window('Welcome to Nulist Idea Mapping Service',
                   layout=[[label], [inputbox, add_btn]],
                   font=('Andale Mono', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.get_todos()
            todos.append(values["todo"] + "\n")
            functions.write(todos)
        case sg.WIN_CLOSED:
            break

window.close()
