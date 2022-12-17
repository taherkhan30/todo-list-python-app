todos = []
while True:
    user_action = input("type and or show or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("enter a todo")
            todos.append(todo)
        case 'show' | 'display':
            for item in todos:
                item = item.title()
                print(item)
        case 'exit':
            break
        case _:
            print("you entered an unknown command")

print("bye")