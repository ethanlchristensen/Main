# Let's create a simple Dictionary
# Remember a dictionary have elements that are of the form key:value.
my_dict = {'Name':'Ethan', 'Age':21, 'School':'UNO', 'Major':'Computer Science'}
print('Printing Dictionary . . .')
print(my_dict,'\n')

# We can use get() to get a value of the given key
# get('School') looks for a key called School and returns its associated value
school = my_dict.get('School')
print('Printing the value associated with the key \'School\' . . .')
print(school)
# We can also get values if we know the key, the key will act as the index. . .
age = my_dict['Age'] # where age is our key
print('Getting the value associated with the key \'Age\'')
print(age, '\n')

# We can use pop() to remove an element with a specific key
# Here we use pop('School') to remove the School key:value pair from our dictionary
my_dict.pop('School')
print('Removing the key:value pair associated with the key \'School\' . . .')
print(my_dict, '\n')

# On the other hand the popitem() will remove the last inserted key pair
# We can see here that the Major key:value pair is removed
my_dict.popitem()
print('Using pop() to remove the last key:value pair . . .')
print(my_dict, '\n')

# Using update() to put back the Major and School key:value pairs we removed
# Here we have to pass in a dict to update . . . i.e. dict.update({key:value, . . .})
my_dict.update({'School':'UNO', 'Major':'Computer Science'})
print('Adding back School:UNO and Major:Computer Science with update() . . .')
print(my_dict, '\n')

# We can use keys() to return a list of all the keys
my_keys = my_dict.keys()
print('Getting the keys from our dictionary with keys() . . .')
print(my_keys, '\n')

# We can use values() to return a list of all the values
my_vals = my_dict.values()
print('Getting the values from our dictionary with value() . . .')
print(my_vals, '\n')

# We can use copy() to return a copy of the dictionary
my_copy = my_dict.copy()
print('Creating a copy of the dictionary with copy() . . .')
print('my_dict: ', my_dict)
print('my_copy: ', my_copy, '\n')

# We can use clear() to clear a dictionary
my_copy.clear()
print('Clearing my_copy dictionary with clear(). . .')
print('my_copy: ', my_copy, '\n')
