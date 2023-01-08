FILEPATH = 'todos.txt'

def get_todos(file_data=FILEPATH):
    with open(file_data,'r') as file:
        todos =  file.readlines()    
    todos = [t.strip('\n') for t in todos]
    return todos

def save_todos(todos,file_data=FILEPATH):
    todos = [t + '\n' for t in todos]
    with open(file_data,'w') as file:
      file.writelines(todos)
    
def print_todos(todos):
    for i in range(len(todos)):
        print(i , ":" , todos[i].strip())

def edit_todo(new_todo, todo_to_edit):
    try:
        todos = get_todos()
        todos[todos.index(todo_to_edit)] = new_todo
        save_todos(todos)
    except:
        print("task number not available")

def add_todo(todo):
    todos = get_todos()
    todos.append(todo)
    save_todos(todos)   

def complete_todo(todo_to_complete):
    try:
        todos = get_todos()
        del todos[todos.index(todo_to_complete)]
        save_todos(todos)
    except:
        print("task number not available")


if __name__ == "__main__":
    print("hello from functions file")
    print_todos(get_todos())