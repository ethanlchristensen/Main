# LEET CODE 66 Plus One
# Given a large integer, represented as a list of digits
# return the result when one is added to the intger as a list

def plusOne(digits):
    carry = 0
    completed = False
    for i in range(len(digits) - 1, -1, -1):
        if completed:
            break
        if digits[i] == 9:
            digits[i] = 0
            if len(digits) == 1:
                carry += 1
                break
            for j in range(i-1, -1, -1):
                if digits[j] == 9:
                    digits[j] = 0
                else:
                    digits[j] += 1
                    completed = True
                    break
                if j == 0:
                    carry += 1
            completed = True
        else:
            digits[i] += 1
            break
    if carry > 0:
        return [1] + digits
    else:
        return digits

def plusOneV2(digits):
    digits = int(''.join([str(d) for d in digits]))
    digits += 1
    res = []
    while digits != 0:
        res.append(digits%10)
        digits = digits // 10
    res = res[::-1]
    return res


def plusOnev3(digits):
    noCarry = False
    p = len(digits) - 1
    while p > -1:
        if digits[p] < 9:
            digits[p] += 1
            noCarry = True
            break
        else:
            digits[p] = 0
            p -= 1
    if noCarry:
        return digits
    else:
        return [1] + digits
        
    
    


test_cases = [[1,2,3],
              [9,9,9],
              [9,9],
              [9],
              [4,3,2,2],
              [4,3,2,1]]
for case in test_cases:
    print("{} + 1 -> {}".format(case, plusOne(list(case))))
for case in test_cases:
    print(plusOneV2(case))

num = [1,2,9]
print(plusOnev3(num))