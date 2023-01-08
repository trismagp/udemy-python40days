from functions import get_todos,print_todos,add_todo,edit_todo,delete_todo
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%A %d.%m.%Y, %H:%M:%S")
print("Current Time =", current_time)

while True:
    
    user_action = input("Pick an action 0.show 1.add, 2.edit, 3.delete, 4.quit:")

    if user_action.startswith("show"):
        print_todos(get_todos())
    elif user_action.startswith("add "):
        add_todo(user_action[4:].strip())
    elif user_action.startswith("edit "):
        edit_todo(user_action[5:].strip())
    elif user_action.startswith("delete "):
        delete_todo(user_action[7:].strip())
    elif user_action.startswith("quit"):
        break
    else:
        print('Command not found. Please type 1,2,3 or 4')

print('bye bye')
