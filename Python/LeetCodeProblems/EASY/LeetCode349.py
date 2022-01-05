# LEET CODE 349 DECODE STRING
# Given a String s, decode it given the following rules . . .
# The string will be of the format k[encoded_string] where
# k is an integer and the endcoded_string will not have any
# numbers. k is the number of times the encoded string will
# be repeated. For example . . . 
# 3[a] = aaa
# 3[a2[bc]] = abcbcabcbcabcbc
# A way to go about this is to solve the inner most part and
# work outwards . . . i.e
# 2[bc] = bcbc
# a2[bc] = abcbc
# 3[a2[bc]] = abcbcabcbcabcbc

def decodeString(s):
    stack = []

    for i in range(len(s)):
        if s[i] != ']':
            stack.append(s[i])
        else:
            substr = ""
            while stack[-1] != '[':
                substr = stack.pop() + substr
            stack.pop()

            k = ""
            while stack and stack[-1].isdigit():
                k = stack.pop() + k
            
            stack.append(int(k) * substr)
    return ''.join(stack)

test_cases = ["3[a]2[bc]" , "3[a2[bc]]", "2[abc]3[cd]ef", "abc3[cd]xyz", "2[ab3[cd4[ef]]]"]
for case in test_cases:
    print("{:<20} -> {:<50}".format(case, decodeString(case)))                             