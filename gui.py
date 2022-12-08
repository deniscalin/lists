import functions
import PySimpleGUI as sg

label = sg.Text("Control your day! Add your todo.")
inputbox = sg.InputText(tooltip="Enter todo")
add_btn = sg.Button("Add")

window = sg.Window('Welcome to Nulist Idea Mapping Service', layout=[[label], [inputbox, add_btn]])
window.read()
window.close()
