# Create a list by taking in 5 user inputted numbers.
nums = []

nums.append(int(input("Enter First Number: ")))
nums.append(int(input("Enter Second Number: ")))
nums.append(int(input("Enter Third Number: ")))
nums.append(int(input("Enter Fourth Number: ")))
nums.append(int(input("Enter Fifth Number: ")))

print('nums: ', nums)

# Now sort the list
nums.sort()
print('Sorted nums: ', nums)

# Now add up all the elements
total = int(sum(nums))
print('Sum: ', total)

# Now remove the thrid element in the list
nums.pop(2)
print('Removed nums[2]: ', nums)

# Now count the number of 5's in the list
total_5 = nums.count(5)
print('Total number of 5\'s: ', total_5)

# Now we will add more 5's and call that method again
nums.append(5)
nums.append(5)
print('nums: ', nums)
total_5 = nums.count(5)
print('Total number of 5\'s: ', total_5)

# Now we will get the index of the first occurance of the number 5
index_5 = nums.index(5)
print('First occurance of the number 5: nums[{:d}]'.format(index_5))