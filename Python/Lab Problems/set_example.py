# Here are some examples with sets.
# Sets are cool in teh fact that they don't contain duplicates
# For example . . .
my_set1 = {1, 1, 2, 3, 4, 5, 6, 7}
my_set2 = set([12, 15, 23, 23, 3, 2, 1, 9, 45])
my_set3 = {'apples', 'bananas', 'pears', 'pears', 'apples', 'oranges'}
print('my_set1:', my_set1, '\nmy_set2:', my_set2, '\nmy_set3:', my_set3, '\n')

# We can add to sets with add()
my_set3.add('kiwis')
print('Adding \'kiwis\' with add() . . .')
print('my_set3:', my_set3, '\n')

# We can find the difference between two sets with difference()
# this has the form x.difference(y) where the returned set are
# elements that are in x and not y. In our case, the elements
# 4, 5, 6, and 7 are in x but not in y so we should expect those
# numbers to be returned
print('Finding the difference between my_set1 and my_set2 with difference() . . .')
my_difference = my_set1.difference(my_set2)
print('Difference:', my_difference)
print('Finding the difference between my_set2 and my_set1 with difference() . . .')
my_difference = my_set2.difference(my_set1)
print('Difference:', my_difference, '\n')

# We can use union() to join to seperate sets
my_union = my_set1.union(my_set2)
print('Joining my_set1 and my_set2 with union() . . .')
print('Union:', my_union, '\n')

# We can use discard() or remove() to remove a specific element.
# Remeber there are no duplicates, so this will
# remove the only instance of that value
print('Removing 45 from our union set with discard() . . .')
my_union.discard(45)
print('Union:', my_union)
print('Removing 23 from our union set with remove() . . .')
my_union.remove(23)
print('Union:', my_union)
print('Removing \'apples\' from my_set3 . . .')
my_set3.remove('apples')
print('my_set3:', my_set3, '\n')

# We can see is a set is a sub-set of another
# with the issubset()
my_sub = {1, 2, 3}
my_sub2 = {16, 28, 75}
if my_sub.issubset(my_set1):
    print('My sub set:', my_sub, 'is present in my_set1:', my_set1, '\n')
else:
    print('My sub set:', my_sub, 'is NOT present in my_set1:', my_set1, '\n')
if my_sub2.issubset(my_set1):
    print('My sub set 2:', my_sub2, 'is present in my_set1:', my_set1, '\n')
else:
    print('My sub set 2:', my_sub2, 'is NOT present in my_set1:', my_set1, '\n')
    
    # We can use intersection() to find similar values between sets
    print('Finding similar values between my_set1 and my_set2 . . .')
    my_similar = my_set1.intersection(my_set2)
    print('my_set1:', my_set1, '\nmy_set2:', my_set2, '\nShared values:', my_similar, '\n')
    