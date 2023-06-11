# creating a list to store todos
todo_list = []

# loop to get inputs
while True:
    user_action = input("Type add or show or exit : ").strip()
    match user_action:
        case 'add':
            # getting the todo item
            todo_item = input("Enter a todo item : ")
            todo_list.append(todo_item)
        case 'show':
            # getting list of todos
            for item in todo_list:
                item = item.title()
                print(item)
        case 'edit':
            # getting the todo item to edit
            number = int(input("Enter the Todo number to edit : "))
            number = number-1
            
            # editing the item
            todo_item = input("Enter the new Todo : ")
            todo_list[number] = todo_item
        case 'exit':
            break
        case undefinedInput:
            print("Invalid Command")

print('Good Bye')
