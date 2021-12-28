choice = 0
user_list = []
while choice != 5:
    print('   [1] Add an element\n   [2] Delete an element\n   [3] Print list\n   [4] Sort list\n   [5] Exit')
    choice = int(input('Choose and option: '))
    
    if choice == 1:
        user_list.append(int(input('Please enter a number to add to your list: ')))
        print()
    elif choice == 2:
        if len(user_list) == 0:
            print('Your list has no elements, please add elements first . . .\n')
        else:
            user_list.remove(int(input('Please enter a number to delete from your list: ')))
            print()
    elif choice == 3:
        if len(user_list) == 0:
            print('Your list has no elements, please add elements first . . .\n')
        else:
            print(user_list)
            print()
    elif choice == 4:
        if len(user_list) == 0:
            print('Your list has no elements, please add elements first . . .\n')
        else:
            user_list = sorted(user_list)
            print()