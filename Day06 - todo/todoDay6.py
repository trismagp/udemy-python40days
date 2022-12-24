file = open('todos.txt','r')
todos =  file.readlines()
todos = [t.strip('\n') for t in todos]
file.close()

def print_todos():
    for i in range(len(todos)):
        print(i , ":" , todos[i].strip())

def update_todo():
    try:
        print_todos()
        todo_num = input('Choose a todo number to update: ')
        todos[int(todo_num)] = input('Enter todo change: ').strip()
    except:
        print("task number not available")
    print_todos()        

def delete_todo():
    print_todos()
    todo_num = input('Choose a todo number to delete: ') 
    del todos[int(todo_num)]
    print_todos()        


while True:
    user_action = input("Pick an action 1.add, 2.update, 3.delete, 4.quit:")

    match user_action:
        case '1':
            todo = input('Enter a todo: ').strip()
            todos.append(todo)
        case '2':
            update_todo()  
        case '3':
            delete_todo()
        case '4':
            break
        case _:
            print('Command not found. Please type 1,2,3 or 4')

print('bye bye')
file = open('todos.txt','w')
todos = [t + '\n' for t in todos]
file.writelines(todos)
file.close()
