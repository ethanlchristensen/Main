def display(): # Display the options a user can choose
    print('1. Add Item')
    print('2. Update Item')
    print('3. Delete Item')
    print('4. Display Cart')
    print('5. Quit')


def get_ans(): # Get user input until it is valid
    out = int(input('Enter the number of your choice: '))
    if out < 1 or out > 5:
        print('Incorrect input. ', end = '')
        out = get_ans()
    return out


def add_item(prices_dict, quantity_dict): # Add an item to the dictionaries
    item = input('Enter the name of the item to add: ')
    price = float(input('Enter the price of the item: '))
    quantity = int(input('Enter the quantity of item to be purchased: '))
    print('Added {} {} with a cost of {} / item . . .\n'.format(quantity, item, price))
    prices_dict.update({item:price})
    quantity_dict.update({item:quantity})
    
    
def delete_item(prices_dict, quantity_dict): # Delete an item from the dictionaries
    if len(prices_dict) > 0:
        item = input('Enter the item to be deleted: ')
        if item in prices_dict:
            prices_dict.pop(item)
            quantity_dict.pop(item)
            print('Removed {} . . .\n'.format(item))
        else:
            print('Item has not been added yet!\n')
    else:
        print('Your cart is empty!\n')
    
    
def update_item(prices_dict, quantity_dict): # Update an exisitng item in the dictionary
    if len(prices_dict) > 0:
        item = input('Enter the name of the item to update: ')
        if item in prices_dict:
            price = float(input('Enter the updated price of the item: '))
            quantity = int(input('Enter the updated quantity of the item: '))
            prices_dict[item] = price
            quantity_dict[item] = quantity
            print('Updated {} with a price of {} and qunatity of {} . . .\n'.format(item, price, quantity))
        else:
            print('Item has not been added yet!')
    else:
        print('Your cart is empty!\n')
        

def display_cart(prices_dict, quantity_dict): # Display everything in the users cart
    if len(prices_dict) > 0:
        items = list(prices_dict.keys())
        prices = list(prices_dict.values())
        quantity = list(quantity_dict.values())
        total = 0
        print()
        for i in range(len(prices_dict)):
            total += quantity[i] * prices[i]
            print('{} ({} at ${:.2f} / item): ${:.2f}'.format(items[i], quantity[i], prices[i], quantity[i] * prices[i]))
        print('\nTotal cost of items in the cart: {:.2f}\n'.format(total))
    else:
        print('Your cart is empty!\n')
    
    


def main():
    prices = {} # This will store each item we add and its assocaited price
    quantity = {} # This will store how much of each item we have
    ans = 0 # This will keep track of what the user wants to do
    print('Welcome to Generic E-Commerce Store!') # Opening prompt
    print('Which of the following would you like to do?')
    while ans != 5: # Keep prompting the user until they hit 5
        display() # Display the options to the user
        ans = get_ans() # Get the answer
        if ans == 1:
            add_item(prices, quantity)
        elif ans == 2:
            update_item(prices, quantity)
        elif ans == 3:
            delete_item(prices, quantity)
        elif ans == 4:
            display_cart(prices, quantity)
    print('Exiting . . .\n')
    

main()