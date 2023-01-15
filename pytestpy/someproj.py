todo = []

def todolist(todo):
    x = 0
    for i in todo:
        x+=1
        print(f"{x} : {i}")
def add_todo(todo, text):
    todo.append(text)

while True:
    task = input("specifiy operation?\n1) add todo\n2) remove todo\n3) list todo\n4) exit\nchoose: ")
    if task == "1":
        text = input("todo: ")
        add_todo(todo, text)
    elif task == "2":
        
        #try:
            print("which todo you want to remove?")
            todolist(todo)
            text = int(input(""))
            text-=1
            del todo[text]
        #except:
            print("number was removed.")
    elif task == "3":
        todolist(todo)
    elif task == "4":
        break
    else:
        print("something went wront")
        break

