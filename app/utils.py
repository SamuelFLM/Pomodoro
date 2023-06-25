import PySimpleGUI as sg

layout = [[sg.Button('Button with Image', image_filename='dependency/img/chevron-up-24.png', expand_x=True)]]
window = sg.Window('Window with Image Button', layout, size=(200,300))

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

window.close()

