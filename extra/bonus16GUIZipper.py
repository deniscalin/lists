import PySimpleGUI as sg
from bonus16ZipCreator import make_archive

label1 = sg.Text("Select files to compress: ")
input1 = sg.Input()
bttn1 = sg.FilesBrowse("Browse", key="files")

label2 = sg.Text("Select destination folder: ")
input2 = sg.Input()
bttn2 = sg.FolderBrowse("Browse", key="folder")

compress_bttn = sg.Button("Compress")
output_notice = sg.Text(key="output", text_color="green")

window = sg.Window("Welcome to Simple Compressor Service!",
                   layout=[[label1, input1, bttn1],
                           [label2, input2, bttn2],
                           [compress_bttn, output_notice]])

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    match event:
        case 'Compress':
            make_archive(filepaths, folder)
            window["output"].update(value="Compression successful")
        case sg.WIN_CLOSED:
            break


window.close()
