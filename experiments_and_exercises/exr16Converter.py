import PySimpleGUI as sg

label1 = sg.Text("Enter feet: ")
box1 = sg.Input()

label2 = sg.Text("Enter inches: ")
box2 = sg.Input()

convert_btn = sg.Button("Convert")

window = sg.Window("Converter", layout=[[label1, box1], [label2, box2], [convert_btn]])
window.read()
print("After read")
window.close()
