# LEET CODE 917 Reverse Only Letters
# Given a String s, return the string with only the letters
# reversed. Other characters should remain in the same position

def reverseOnlyLetter(s):
    s = [c for c in s]
    l, r = 0, len(s) - 1
    while l < r:
        if s[l].isalpha() and s[r].isalpha():
            tmp = s[r]
            s[r] = s[l]
            s[l] = tmp
            l += 1
            r -= 1
        elif s[l].isalpha():
            r -= 1
        elif s[r].isalpha():
            l += 1
        else:
            l += 1
            r -= 1
    return ''.join(s)


string = "ab-cd"
print("{} <-> {}".format(string, reverseOnlyLetter(string)))
string2 = "a-bC-dEf-ghIj"
print("{} <-> {}".format(string2, reverseOnlyLetter(string2)))
string3 = "Test1ng-Leet=code-Q!"
print("{} <-> {}".format(string3, reverseOnlyLetter(string3)))
