# LEET CODE 58 Length of Last Word
# given a string s containing words seperated by spaces
# return the lenght of the last word in the string

def lengthOfLastWord(s):
    return len([w for w in s.split(" ") if w != ""][-1])


test_cases = ["Hello World","   fly me   to   the     moon  ","luffy is still joyboy"]
for case in test_cases:
    print("{} --> {}".format(case, lengthOfLastWord(case)))
