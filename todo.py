# creating a list to store todos
todo_list = []

# loop to get inputs
while True:
    user_action = input("Type add,show,edit,complete or exit : ").strip()
    match user_action:
        case 'add':
            # getting the todo item
            todo_item = input("Enter a todo item : ")
            todo_list.append(todo_item)
        case 'show':
            # getting list of todos
            for index,item in enumerate(todo_list):
                item = item.title()

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
