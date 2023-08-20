todos = []

def get_todos():
    return todos

def add_todo(todo):
    todos.append(todo)

def delete_todo(index):
    if 0<= index <len(todos):
        del todos[index]

def modify_todo(index, new_todo):
    if 0<= index <len(todos):
        todos[index]['text']= new_todo
