from functions import get_todos,print_todos,add_todo,edit_todo,delete_todo
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo", key = 'todo')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=get_todos(),key='todos',enable_events=True,size=[45,10])
edit_button = sg.Button("Edit")

window = sg.Window('My To-Do App',
                layout=[[label],[input_box,add_button],[list_box,edit_button]],
                font=('Helvetica',16))

while True:
    event, value = window.read()
    match event:
        case "Add":
            add_todo(value['todo'].strip())
            window['todos'].update(values=get_todos())
        case "Edit":
            new_todo = value['todo'].strip()
            todo_to_edit = value['todos'][0].strip()
            edit_todo(new_todo,todo_to_edit)
            window['todos'].update(values=get_todos())
        case sg.WIN_CLOSED:
            break

window.close()