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
    try:
        todos = get_todos()
        removed_todo =  todos[int(todo_num)] 
        del todos[int(todo_num)]
        print_todos(todos)
        save_todos(todos)        
        print(f"Todo {removed_todo} was removed")
    except:
        print("task number not available")
