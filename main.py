todos = []
while True:
    user_action = input("type add, edit, show or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("enter a todo: ")
            todos.append(todo)
        case 'show' | 'display':
            for item in todos:
                item = item.title()
                print(item)
        case 'edit':
            number = int(input('which task number do you want to edit?: '))
            number = number - 1
            new_todo = input('enter new todo: ')
            todos[number] = new_todo
        case 'exit':
            break
        case _:
            print("you entered an unknown command")
print("bye")

