# LEET CODE 231 POWER OF TWO
# Given a number n, determine if that number
# is a power of two . . . For example,
# 8  = 2 ^ 3 = True
# 16 = 2 ^ 4 = True
# 9  = 3 ^ 2 = False

def isPowerOfTwo(n):
    if n == 0:
        return False
    while n != 1:
        if n % 2 != 0:
            return False
        n = n / 2
    return True


test_cases = [2,4,16,8,23,14,536870912]
print("==============TESTING==============")
for case in test_cases:
    if isPowerOfTwo(case):
        print('{:<15} {:<20}'.format(case, 'is a power of 2.'))
    else:
        print('{:<15} {:<20}'.format(case, 'is not a power of 2.'))