# LEET CODE 997 Find the Town Judge
# Given an array of trust relations determine who the
# town judge is given that the judge trusts no one and
# everyone trusts the judge

def findJudge(n, trust):
    h = {}
    for i in range(n):
        h[i+1] = []
    for i in range(len(trust)):
        h[trust[i][0]].append(trust[i][1])
    possibleJudge = -1
    for key in h:
        if h[key] == []:
            h.pop(key)
            possibleJudge = key
            break
    for key in h:
        if not(possibleJudge in h[key]):
            return -1
    return possibleJudge
    
        

relations = [[1,2]]
print(findJudge(2, relations))