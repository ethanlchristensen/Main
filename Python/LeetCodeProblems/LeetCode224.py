# LEET CODE 224 BASIC CALCULATOR
# Given a string perform the operation
# "1 + 4"
# "2 - 1 + 2"
# "(1 + (4 + 5 + 2) - 3) + (6 + 8)"

def calculate(s):
    stack = []
    buf_stack = []
    num = ""
    for i in range(len(s)):
        if s[i] == ")":
            c = stack.pop()
            while c != '(':
                buf_stack.append(c)
                c = stack.pop()
            buf_stack.reverse()
            res = 0
            for j in range(0, len(buf_stack), 2):
                if j == 0:
                    if buf_stack[j].isdigit():
                        res = int(buf_stack[j]) # SHOULD ALWAYS BE TRUE
                else:
                    if buf_stack[j-1] == '+':
                        res += int(buf_stack[j])
                    elif buf_stack[j-1] == '-':
                        res -= int(buf_stack[j])
            stack.append(str(res))
            buf_stack = []
        else:
            if s[i] != ' ':
                if s[i].isdigit():
                    num += s[i]
                    if i == len(s) - 1:
                        stack.append(num)
                        num = ""
                    elif not s[i+1].isdigit():
                        stack.append(num)
                        num = ""
                else:
                    if num != "":
                        stack.append(num)
                        stack.append(s[i])
                        num = ""
                    else:
                        stack.append(s[i])
    res = 0
    if len(stack) > 1:
        for i in range(0,len(stack),2):
            if i == 0:
                res = int(stack[i])
            else:
                if stack[i-1] == '+':
                    res += int(stack[i])
                elif stack[i-1] == '-':
                    res -= int(stack[i])
        return res
    else:
        return stack[0]


test_cases = ["(1+(4+5+2)-3)+(6+8)", " 2-1 + 2 ", "1 + 1"]
for case in test_cases:
    print(calculate(case))