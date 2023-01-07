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

def update_todo():
    try:
        todos = get_todos()
        print_todos(todos)
        todo_num = input('Choose a todo number to update: ')
        todos[int(todo_num)] = input('Enter todo change: ').strip()
        save_todos(todos)
        print_todos(todos)
    except:
        print("task number not available")

def add_todo():
    todos = get_todos()
    print_todos(todos)
    todo = input('Enter a todo: ').strip()
    todos.append(todo)
    save_todos(todos)
    print_todos(todos)    

def delete_todo():
    todos = get_todos()
    print_todos(todos)
    todo_num = input('Choose a todo number to delete: ') 
    del todos[int(todo_num)]
    print_todos(todos)
    save_todos(todos)        


while True:
    user_action = input("Pick an action 1.add, 2.update, 3.delete, 4.quit:")

    match user_action:
        case '1':
            add_todo()
        case '2':
            update_todo()  
        case '3':
            delete_todo()
        case '4':
            break
        case _:
            print('Command not found. Please type 1,2,3 or 4')

print('bye bye')
