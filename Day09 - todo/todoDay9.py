file_data = 'todos.txt'

def get_todos():
    with open(file_data,'r') as file:
        todos =  file.readlines()    
    todos = [t.strip('\n') for t in todos]
    return todos

def save_todos(todos):
    todos = [t + '\n' for t in todos]
    with open(file_data,'w') as file:
      file.writelines(todos)
    
def print_todos(todos):
    for i in range(len(todos)):
        print(i , ":" , todos[i].strip())

def edit_todo(todo_num):
    try:
        todos = get_todos()
        print_todos(todos)
        todos[int(todo_num)] = input('Enter todo change: ').strip()
        save_todos(todos)
        print_todos(todos)
    except:
        print("task number not available")

def add_todo(todo):
    todos = get_todos()
    todos.append(todo)
    save_todos(todos)
    print_todos(todos)    

def delete_todo(todo_num ):
    todos = get_todos()
    removed_todo =  todos[int(todo_num)] 
    del todos[int(todo_num)]
    print_todos(todos)
    save_todos(todos)        
    print(f"Todo {removed_todo} was removed")

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
