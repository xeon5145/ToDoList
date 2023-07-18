# loop to get inputs
while True:
    user_action = input("Type add,show,edit,complete or exit : ").strip()
    match user_action:
        case 'add':
            # getting the todo item
            todo_item = input("Enter a todo item : ") + "\n"

            # now reading todo items from the file
            with open('todo.txt','r') as file: # with context manager we don't have to close the file
                todo_list = file.readlines()

            todo_list.append(todo_item)

            # writing todos in the text file
            file = open('todo.txt', 'w')
            file.writelines(todo_list)
        case 'show':
            file = open('todo.txt','r')
            todo_list = file.readlines()
            file.close()

            # getting list of todos
            for index,item in enumerate(todo_list):
                item = item.title().strip('\n')
                # making item coutn to start form 1 instead of 0
                index = index+1
                data = f"{index}. {item}"
                print(data)

        case 'edit':
            # getting the todo item to edit
            number = int(input("Enter the Todo number to edit : "))
            number = number-1
            
            # editing the item
            todo_item = input("Enter the new Todo : ")
            todo_list[number] = todo_item
        case 'complete':
             # getting the todo item to mark as complete
            number = int(input("Enter the Todo number to complete : "))
            number = number-1

            # marking item as complete
            todo_list.pop(number)
        case 'exit':
            break
        case undefinedInput:
            print("Invalid Command")

print('Good Bye')
