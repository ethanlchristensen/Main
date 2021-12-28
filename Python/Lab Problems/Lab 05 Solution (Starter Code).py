print('Welcome to The Generic Retaurant. Here is our step-by-step menu:')
cusine = input('Which cuisine would you prefer? American, Chinese, Indian, or Mexican: ')

# Start of the American Section
if cusine == 'American':
    meat = input('Which meat would you like? We have Beef, Chicken, Pork, or None: ')
    if meat == 'Beef':
        meal = input('What meal were you thinking? We have Steak or Burger: ')
        if meal == 'Steak':
            side = input('What side would you like? We have Baked Potato or Baked Beans: ')
            if side == 'Baked Potato':
                print('Thank you for ordering a {:s} with {:s}!'.format(meal, side))
            elif side == 'Baked Beans':
                print('Thank you for ordering a {:s} with {:s}!'.format(meal, side))
            else:
                print('That was not an option. Please start from the beginning of the menu.')
        elif meal == 'Burger':
            side = input('What side would you like? We have Fries or Baked Beans: ')
            if side == 'Fries':
                print('Thank you for ordering a {:s} with {:s}!'.format(meal, side))
            elif side == 'Baked Beans':
                print('Thank you for ordering a {:s} with {:s}!'.format(meal, side))
            else:
                print('That was not an option. Please start from the beginning of the menu.')
        else:
            print('That was not an option. Please start from the beginning of the menu.')
    elif meat == 'Chicken':
        meal = input('What meal were you thinking? We have Chicken Parmesan or Chicken Strips: ')
        if meal == 'Chicken Parmesan':
            side = input('What side would you like? We have Soup or Salad: ')
            if side == 'Soup':
                print('Thank you for ordering a {:s} with {:s}!'.format(meal, side))
            elif side == 'Salad':
                print('Thank you for ordering a {:s} with {:s}!'.format(meal, side))
            else:
                print('That was not an option. Please start from the beginning of the menu.')
        elif meal == 'Chicken Strips':
            side = input('What side would you like? We have Fries or Tater Tots: ')
            if side == 'Fires':
                print('Thank you for ordering a {:s} with {:s}!'.format(meal, side))
            elif side == 'Tater Tots':
                print('Thank you for ordering a {:s} with {:s}!'.format(meal, side))
            else:
                print('That was not an option. Please start from the beginning of the menu.')
        else:
            print('That was not an option. Please start from the beginning of the menu.')
    elif meat == 'Pork':
        meal = input('What meal were you thinking? We have Pork Chops or BBQ Pulled Pork Sandwich: ')
        if meal == 'Pork Chops':
            side = input('What side were you thinking? We have Green Beans or Mashed Potatos: ')
            if side == 'Green Beans' or side == 'Mashed Potatos':
                print('Thank you for ordering a {:s} with {:s}!'.format(meal, side))
            else:
                print('That was not an option. Please start from the beginning of the menu.')
        elif meal == 'BBQ Pulled Pork Sandwich':
            side = input('What side were you thinking? We have Baked Beans or Fries: ')
            if side == 'Baked Beans' or side == 'Fries':
                print('Thank you for ordering a {:s} with {:s}!'.format(meal, side))
            else:
                print('That was not an option. Please start from the beginning of the menu.') 
        else:
            print('That was not an option. Please start from the beginning of the menu.')
    elif meat == 'None':
        meal = input('What meal were you thinking? We have Veggie Burgers or Roasted Sweet Potato Salad: ')
        if meal == 'Veggie Burger':
            side = input('What side were you thinking? We have Fresh Fruit or Steamed Broccoli: ')
            if side == 'Fresh Fruit' or side == 'Steamed Broccoli':
                print('Thank you for ordering a {:s} with {:s}!'.format(meal, side))
            else:
                print('That was not an option. Please start from the beginning of the menu.')
        elif meal == 'Roasted Sweet Potato Salad':
            side = input('What side were you thinking? We have Fresh Fruit or Steamed Broccoli: ')
            if side == 'Fresh Fruit' or side == 'Steamed Broccoli':
                print('Thank you for ordering a {:s} with {:s}!'.format(meal, side))
            else:
                print('That was not an option. Please start from the beginning of the menu.') 
        else:
            print('That was not an option. Please start from the beginning of the menu.')
    else:
        print('That was not an option. Please start from the beginning of the menu.')
       
# Start of the Chinese Section
elif cusine == 'Chinese':
    meat = input('Which meat would you like? We have Beef, Chicken, Pork, or None: ')
    if meat == 'Beef':
        meal = input('What meal were you thinking? We have Mongolian Beef or Beef with Broccoli: ')
        if meal == 'Mongolian Beef':
            side = input('What side would you like? We have Fried Rice or Lo Mein: ')
            if side == 'Fried Rice' or side == 'Lo Mein':
                print('Thank you for ordering a {:s} with {:s}!'.format(meal, side))
            else:
                print('That was not an option. Please start from the beginning of the menu.') 
        elif meal == 'Beef with Broccoli':
            side = input('What side would you like? We have Fried Rice or Lo Mein: ')
            if side == 'Fried Rice' or side == 'Lo Mein':
                print('Thank you for ordering a {:s} with {:s}!'.format(meal, side))
            else:
                print('That was not an option. Please start from the beginning of the menu.')
        else:
            print('That was not an option. Please start from the beginning of the menu.')
    elif meat == 'Chicken':
        meal = input('What meal were you thinking? We have Sweet Sour Chicken or Chicken with Broccoli: ')
        if meal == 'Sweet Sour Chicken':
            side = input('What side would you like? We have Fried Rice or Lo Mein: ')
            if side == 'Fried Rice' or side == 'Lo Mein':
                print('Thank you for ordering a {:s} with {:s}!'.format(meal, side))
            else:
                print('That was not an option. Please start from the beginning of the menu.')
        elif meal == 'Chicken with Broccoli':
            side = input('What side would you like? We have Fried Rice or Lo Mein: ')
            if side == 'Fried Rice' or side == 'Lo Mein':
                print('Thank you for ordering a {:s} with {:s}!'.format(meal, side))
            else:
                print('That was not an option. Please start from the beginning of the menu.')
        else:
            print('That was not an option. Please start from the beginning of the menu.')
    elif meat == 'Pork':
        meal = input('What meal were you thinking? We have Black Pepper Pork or Pork with Broccoli: ')
        if meal == 'Black Pepper Prok':
            side = input('What side would you like? We have Fried Rice or Lo Mein: ')
            if side == 'Fried Rice' or side == 'Lo Mein':
                print('Thank you for ordering a {:s} with {:s}!'.format(meal, side))
            else:
                print('That was not an option. Please start from the beginning of the menu.')
        elif meal == 'Pork with Broccoli':
            side = input('What side would you like? We have Fried Rice or Lo Mein: ')
            if side == 'Fried Rice' or side == 'Lo Mein':
                print('Thank you for ordering a {:s} with {:s}!'.format(meal, side))
            else:
                print('That was not an option. Please start from the beginning of the menu.')
        else:
            print('That was not an option. Please start from the beginning of the menu.')
    elif meat == 'None':
        meal = input('What meal were you thinking? We have Mixed Vegtables or Tofu: ')
        if meal == 'Mixed Vegtables':
            side = input('What side would you like? We have Fried Rice or Lo Mein: ')
            if side == 'Fried Rice' or side == 'Lo Mein':
                print('Thank you for ordering a {:s} with {:s}!'.format(meal, side))
            else:
                print('That was not an option. Please start from the beginning of the menu.')
        elif meal == 'Tofu':
            side = input('What side would you like? We have Fried Rice or Lo Mein: ')
            if side == 'Fried Rice' or side == 'Lo Mein':
                print('Thank you for ordering a {:s} with {:s}!'.format(meal, side))
            else:
                print('That was not an option. Please start from the beginning of the menu.')
        else:
            print('That was not an option. Please start from the beginning of the menu.')
    else:
        print('That was not an option. Please start from the beginning of the menu.')
# Start of the Indian Section
elif cusine == 'Indian':
    meat = input('Which meat would you like? We have Beef, Chicken, Pork, or None: ')
    if meat == 'Beef':
        meal = input('What meal were you thinking? We have Beef Curry with Potatoes or Keema Aloo: ')
        if meal == 'Beef Curry with Potatoes':
            side = input('What side would you like? We have Basmati Rice or Naan Bread: ')
            if side == 'Basmati Rice' or side == 'Naan Bread':
                print('Thank you for ordering a {:s} with {:s}!'.format(meal, side))
            else:
                print('That was not an option. Please start from the beginning of the menu.')
        elif meal == 'Keema Aloo':
            side = input('What side would you like? We have Basmati Rice or Naan Bread: ')
            if side == 'Basmati Rice' or side == 'Naan Bread':
                print('Thank you for ordering a {:s} with {:s}!'.format(meal, side))
            else:
                print('That was not an option. Please start from the beginning of the menu.')
        else:
            print('That was not an option. Please start from the beginning of the menu.') 
    elif meat == 'Chicken':
        meal = input('What meal were you thinking? We have Butter Chicken or Chicken Korma: ')
        if meal == 'Butter Chicken':
            side = input('What side would you like? We have Basmati Rice or Naan Bread: ')
            if side == 'Basmati Rice' or side == 'Naan Bread':
                print('Thank you for ordering a {:s} with {:s}!'.format(meal, side))
            else:
                print('That was not an option. Please start from the beginning of the menu.')
        elif meal == 'Chicken Korma':
            side = input('What side would you like? We have Basmati Rice or Naan Bread: ')
            if side == 'Basmati Rice' or side == 'Naan Bread':
                print('Thank you for ordering a {:s} with {:s}!'.format(meal, side))
            else:
                print('That was not an option. Please start from the beginning of the menu.')
        else:
            print('That was not an option. Please start from the beginning of the menu.')
    elif meat == 'Pork':
        meal = input('What meal were you thinking? We have Sorpotel or Naga Pork Curry: ')
        if meal == 'Sorpotel':
            side = input('What side would you like? We have Basmati Rice or Naan Bread: ')
            if side == 'Basmati Rice' or side == 'Naan Bread':
                print('Thank you for ordering a {:s} with {:s}!'.format(meal, side))
            else:
                print('That was not an option. Please start from the beginning of the menu.')
        elif meal == 'Naga Pork Curry':
            side = input('What side would you like? We have Basmati Rice or Naan Bread: ')
            if side == 'Basmati Rice' or side == 'Naan Bread':
                print('Thank you for ordering a {:s} with {:s}!'.format(meal, side))
            else:
                print('That was not an option. Please start from the beginning of the menu.')
        else:
            print('That was not an option. Please start from the beginning of the menu.')
    elif meat == 'None':
        meal = input('What meal were you thinking? We have Chickpea Curry or Masoor Dal: ')
        if meal == 'Chickpea Curry':
            side = input('What side would you like? We have Basmati Rice or Naan Bread: ')
            if side == 'Basmati Rice' or side == 'Naan Bread':
                print('Thank you for ordering a {:s} with {:s}!'.format(meal, side))
            else:
                print('That was not an option. Please start from the beginning of the menu.')
        elif meal == 'Masoor Dal':
            side = input('What side would you like? We have Basmati Rice or Naan Bread: ')
            if side == 'Basmati Rice' or side == 'Naan Bread':
                print('Thank you for ordering a {:s} with {:s}!'.format(meal, side))
            else:
                print('That was not an option. Please start from the beginning of the menu.')
        else:
            print('That was not an option. Please start from the beginning of the menu.')
    else:
        print('That was not an option. Please start from the beginning of the menu.')
# Start of the Mexican Section
elif cusine == 'Mexican':
    meat = input('Which meat would you like? We have Beef, Chicken, Pork, or None: ')
    if meat == 'Beef':
        meal = input('What meal were you thinking? We have Beef Enchiladas or Stuffed Green Pepper: ')
        if meal == 'Beef Enchiladas':
            side = input('What side would you like? We have Mexican Style Rice or Chips and Queso: ')
            if side == 'Mexican Style Rice' or side == 'Chips and Queso':
                print('Thank you for ordering a {:s} with {:s}!'.format(meal, side))
            else:
                print('That was not an option. Please start from the beginning of the menu.')
        elif meal == 'Stuffed Green Pepper':
            side = input('What side would you like? We have Mexican Style Rice or Chips and Queso: ')
            if side == 'Mexican Style Rice' or side == 'Chips and Queso':
                print('Thank you for ordering a {:s} with {:s}!'.format(meal, side))
            else:
                print('That was not an option. Please start from the beginning of the menu.')
        else:
            print('That was not an option. Please start from the beginning of the menu.')
    elif meat == 'Chicken':
        meal = input('What meal were you thinking? We have Chicken Enchiladas or Chicken Quesadilla: ')
        if meal == 'Chicken Enchiladas':
            side = input('What side would you like? We have Mexican Style Rice or Chips and Queso: ')
            if side == 'Mexican Style Rice' or side == 'Chips and Queso':
                print('Thank you for ordering a {:s} with {:s}!'.format(meal, side))
            else:
                print('That was not an option. Please start from the beginning of the menu.')
        elif meal == 'Chicken Quesadilla':
            side = input('What side would you like? We have Mexican Style Rice or Chips and Queso: ')
            if side == 'Mexican Style Rice' or side == 'Chips and Queso':
                print('Thank you for ordering a {:s} with {:s}!'.format(meal, side))
            else:
                print('That was not an option. Please start from the beginning of the menu.')
        else:
            print('That was not an option. Please start from the beginning of the menu.')
    elif meat == 'Pork':
        meal = input('What meal were you thinking? We have Carnitas or Pork Chile Pozole: ')
        if meal == 'Carnitas':
            side = input('What side would you like? We have Mexican Style Rice or Chips and Queso: ')
            if side == 'Mexican Style Rice' or side == 'Chips and Queso':
                print('Thank you for ordering a {:s} with {:s}!'.format(meal, side))
            else:
                print('That was not an option. Please start from the beginning of the menu.')
        elif meal == 'Pork Chile Pozole':
            side = input('What side would you like? We have Mexican Style Rice or Chips and Queso: ')
            if side == 'Mexican Style Rice' or side == 'Chips and Queso':
                print('Thank you for ordering a {:s} with {:s}!'.format(meal, side))
            else:
                print('That was not an option. Please start from the beginning of the menu.')
        else:
            print('That was not an option. Please start from the beginning of the menu.')
    elif meat == 'None':
        meal = input('What meal were you thinking? We have Spicy Cauliflower Tacos or Black Bean Enchiladas: ')
        if meal == 'Spicy Cauliflower Tacos':
            side = input('What side would you like? We have Mexican Style Rice or Chips and Queso: ')
            if side == 'Mexican Style Rice' or side == 'Chips and Queso':
                print('Thank you for ordering a {:s} with {:s}!'.format(meal, side))
            else:
                print('That was not an option. Please start from the beginning of the menu.')
        elif meal == 'Black Bean Enchiladas':
            side = input('What side would you like? We have Mexican Style Rice or Chips and Queso: ')
            if side == 'Mexican Style Rice' or side == 'Chips and Queso':
                print('Thank you for ordering a {:s} with {:s}!'.format(meal, side))
            else:
                print('That was not an option. Please start from the beginning of the menu.')
        else:
            print('That was not an option. Please start from the beginning of the menu.')
    else:
        print('That was not an option. Please start from the beginning of the menu.')
else:
    print('That was not an option. Please start from the beginning of the menu.')