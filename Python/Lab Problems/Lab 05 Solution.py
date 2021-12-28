print('Welcome to The Generic Restaurant. Here is our step-by-step menu: ')
cuisine = input('Which cuisine would you prefer? American, Chinese, Indian, or Mexican: ')
error = 'That was not an option. Please start from the beginning of the menu.'

# American Cusine
if cuisine == 'American':
    meat_choice = input('Which meat would you like? We have Beef, Chicken, Pork, or None: ')
    if meat_choice == 'Beef':
        meal = input('What stlye of meal would you like? We have Runza or a Burger: ')
        if meal == 'Runza':
            side = input('What kind of side do you want with your meal? We have Fries or More Fries: ')
            if side == 'Fries' or side == 'More Fries':
                print(f'Thank you for ordering a {meal} and {side}.')            
            else:
                print(error)
        elif meal == 'Burger':
            side = input('What kind of side do you want with your meal? We have Onion Rings and Less Fries: ')
            if side == 'Onion Rings' or side == 'Less Fries':
                print(f'Thank you for ordering a {meal} and {side}.')
            else:
                print(error)
        else:
            print(error)
    elif meat_choice == 'Chicken':
        meal = input('What kind of meal were you thinking? We have Chicken Sandwich or Chicken Wrap: ')
        if meal == 'Chicken Sandwich':
            side = input('What kind of side do you want with your meal? We have Chips or Carrots: ')
            if side == 'Chips':
                print(f'Thank you for ordering a {meal} and {side}.')
            elif side == 'Carrots':
                print(f'Thank you for ordering a {meal} and {side}.')
            else:
                print(error)
        elif meal == 'Chicken Wrap':
            side = input('What kind of side do you want with your meal? We have Salad or Cheese Bread: ')
            if side == 'Salad':
                print(f'Thank you for ordering a {meal} and {side}.')
            elif side == 'Cheese Bread':
                print(f'Thank you for ordering a {meal} and {side}.')
            else:
                print(error)
        else:
            print(error)
    elif meat_choice == 'Pork':
        meal = input('What stlye of meal would you like? We have Grilled Pork or Pork Ribs: ')
        if meal == 'Grilled Pork':
            side = input('What kind of side do you want with your meal? We have Pulled Pork or Mashed Potatoes: ')
            if side == 'Pulled Pork' or side == 'Mashed Potatoes':
                print(f'Thank you for ordering a {meal} and {side}.')            
            else:
                print(error)
        elif meal == 'Pork Ribs':
            side = input('What kind of side do you want with your meal? We have Cornbread or Potato Salad or Coleslaw: ')
            if side == 'Cornbread' or side == 'Potato Salad' or side == 'Coleslaw':
                print(f'Thank you for ordering a {meal} and {side}.')
            else:
                print(error)
        else:
            print(error)
    elif meat_choice == 'None':
        meal = input('What stlye of meal would you like? We have Salad or Mac and Cheese: ')
        if meal == 'Salad':
            side = input('What kind of side do you want with your meal? We have Potato Soup or Baked Potato: ')
            if side == 'Potato Soup' or side == 'Baked Potato':
                print(f'Thank you for ordering a {meal} and {side}.')            
            else:
                print(error)
        elif meal == 'Mac and Cheese':
            side = input('What kind of side do you want with your meal? We have Garlic Bread or Cheese Bread or Bread: ')
            if side == 'Garlic Bread' or side == 'Cheese Bread' or side == 'Bread':
                print(f'Thank you for ordering a {meal} and {side}.')
            else:
                print(error)
        else:
            print(error)
    else:
        print(error)
# Chinese Cuisine
elif cuisine == 'Chinese':
    print(cuisine)
# Indian Cuisine
elif cuisine == 'Indian':
    print(cuisine)
# Mexican Cuisine
elif cuisine == 'Mexican':
    print(cuisine)
else:
    print(error)
    