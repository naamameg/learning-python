def menu():
    grocery_list = []
    list_1 = input('enter your list here\n').split(',')
    for word in list_1:
        grocery_list.append(word)
        number = 0
    while number != 9:
        number = int(input('enter a number between 1 and 9\n'))
        if number == 1:
            menu_option_1(grocery_list)
        elif number == 2:
            menu_option_2(grocery_list)
        elif number == 3:
            menu_option_3(grocery_list)
        elif number == 4:
            menu_option_4(grocery_list)
        elif number == 5:
            menu_option_5(grocery_list)
        elif number == 6:
            menu_option_6(grocery_list)
        elif number == 7:
            menu_option_7(grocery_list)
        elif number == 8:
            menu_option_8(grocery_list)
    print('Goodbye!')


#1
def menu_option_1(grocery_list):
    print(grocery_list)


#2
def menu_option_2(grocery_list):
    print('You have ' + str(len(grocery_list)) + ' item in your list')

#3
def menu_option_3(grocery_list):
    item = input('enter an item to check\n')
    if item in grocery_list:
        print('Item in grocery list')
    else:
        print('Item is not in grocery_list')

#4
def menu_option_4(grocery_list):
    user_item = input('enter item to check count in list\n')
    counter = 0
    for item in grocery_list:
        if item == user_item:
            counter +=1
    print('Item in list ' + str(counter) + ' times')

#5
def menu_option_5(grocery_list):
    user_item= input('enter an item to delete\n')
    grocery_list.remove(user_item)

#6
def menu_option_6(grocery_list):
    user_item = input('enter an item to add\n')
    grocery_list.append(user_item)

#7
def menu_option_7(grocery_list):
    not_legal_items = []
    for item in grocery_list:
        if len(item) < 3:
            not_legal_items.append(item)
        else:
            for letter in item:
                if not letter.isalpha():
                    not_legal_items.append(item)
                    break
    print(not_legal_items)

#8
def menu_option_8(grocery_list):
    new_list = []
    indexes_to_remove = []
    for index in range(len(grocery_list)):
        if not grocery_list[index] in new_list:
            new_list.append(grocery_list[index])
        else:
            indexes_to_remove.append(index)
    for i in range(len(indexes_to_remove)-1,-1,-1):
        del grocery_list[indexes_to_remove[i]]

menu()