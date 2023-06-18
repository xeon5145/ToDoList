list = ['almighty','binny','slick','knight','ortho']
# sorting list in alphabetical order
list.sort()

# print the list with indexes
for i,j in enumerate(list):
    item = f"{i+1}.{j.capitalize()}"
    print(item)