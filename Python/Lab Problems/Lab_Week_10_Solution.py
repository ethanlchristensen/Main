def display():
    print('1. Add Item')
    print('2. Update Item')
    print('3. Delete Item')
    print('4. Display Items by Name')
    print('5. Quit')


def main():
    print('Welcome to Generic E-Commerce Store!')
    print('Which of the following would you like to do?')
    ans = 0
    while ans != 5:
        display()
        ans = int(input('Enter your choice: '))

main()
