import PySimpleGUI as sg

sg.theme('BluePurple')

layout = [[sg.Text('Your typed chars appear here:'), sg.Text(size=(15,1), key='-OUTPUT-')],
           [sg.Input(key='-IN-')],
           [sg.Button('Show'), sg.Button('Exit')]]

window = sg.Window('Pattern 2B', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.Win_closed or event == 'Exit':
        break
    if event == 'Show':
        window['-Output-'].update(values['-IN-'])

window.close()