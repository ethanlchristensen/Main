# LEET CODE 66 Plus One
# Given a large integer, represented as a list of digits
# return the result when one is added to the intger as a list

def plusOne(digits):
    for i in range(len(digits)-1,-1,-1):
        if digits[i] == 9:
            digits[i] == 0
            for j in range(i-1, -1, -1):
                if digits[j] < 9:
                    digits[j] += 1
                    break
                digits[j] = 0
        digits[i] += 1
        break
    


num = [1,2,3]
plusOne(num)
print(num)