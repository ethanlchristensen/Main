# LEET CODE 210 COURSE SCHEDULE II
# Given the number of courses and a list that
# contains pairs or courses like [x , y] where
# y must be taken first in order to take x. 
# return an array of the order the classes should
# be taken or return an empty one if impossible.

def findOrder( numCourses, prerequisites ):
    out = []
    required = {}
    for p in prerequisites:
        if p[0] not in required:
            required[p[0]] = [p[1]]
        else:
            required[p[0]].append(p[1])
    return required
    
n = 4
courses = [[1,0], [2,0], [3,1], [3,2]]
out = findOrder(n, courses)
print(out)
    