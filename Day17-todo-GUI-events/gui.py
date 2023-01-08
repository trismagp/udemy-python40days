from functions import get_todos,print_todos,add_todo,edit_todo,delete_todo
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo", key = 'todo')
add_button = sg.Button("Add")

window = sg.Window('My To-Do App',
                layout=[[label],[input_box,add_button]],
                font=('Helvetica',16))

while True:
    event, value = window.read()
    print(value)
    match event:
        case "Add":
            add_todo(value['todo'].strip())
        case sg.WIN_CLOSED:
            break

window.close()