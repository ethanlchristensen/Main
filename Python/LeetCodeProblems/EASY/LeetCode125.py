# LEET CODE 125 Valid Palindrome
# given a string return whether or not the string is a valid palindrome
# by first removing all non-alphanumeric characters.

def isPalindrome(s):
    l, r = 0, len(s) - 1
    while l < r:
        if s[l].isalnum() and s[r].isalnum():
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        else:
            if s[l].isalnum() != True:
                l += 1
            if s[r].isalnum() != True:
                r -= 1
    return True

word = "A man, a plan, a canal: Panama" # should be one
print("{} -> {}".format(word, isPalindrome(word)))
word = "race a car" # should not be one
print("{} -> {}".format(word, isPalindrome(word)))
        