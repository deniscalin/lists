import PySimpleGUI as sg

label1 = sg.Text("Select files to compress: ")
input1 = sg.Input()
bttn1 = sg.FilesBrowse("Browse")

label2 = sg.Text("Select destination folder: ")
input2 = sg.Input()
bttn2 = sg.FolderBrowse("Browse")

compress_bttn = sg.Button("Compress")

window = sg.Window("Welcome to Simple Compressor Service!", layout=[[label1, input1, bttn1], [label2, input2, bttn2], [compress_bttn]])
window.read()
window.close()
