# LEET CODE 100 Same Tree
# Given the roots of two binary trees p and q, write
# a function to check if they are the same or not . . .
from BinaryTree import BinaryNode

def isSameTree(p, q): # solution one
    def process(node):
        res = []
        def helper(node):
            if node == None:
                res.append("NULL")
                return
            res.append(node.val)
            helper(node.left)
            helper(node.right)
        helper(node)
        return res
    tree1 = process(p)
    tree2 = process(q)
    print(tree1)
    print(tree2)
    return tree1 == tree2

def isSameTreeV2(p, q): # updated solution
    def helper(n1, n2):
        if n1 == None and n2 == None:
            return True
        if n1 == None and n2 != None:
            return False
        if n1 != None and n2 == None:
            return False
        if n1.val == n2.val:
            return helper(n1.left, n2.left) and helper(n1.right, n2.right)
        else:
            return False
    res = helper(p, q)
    return res


t1 = BinaryNode(1, BinaryNode(2), BinaryNode(3))
t2 = BinaryNode(1, BinaryNode(2), BinaryNode(3))
t3 = BinaryNode(1, BinaryNode(2), BinaryNode(9))
t4 = BinaryNode(1, BinaryNode(2), None)
t5 = BinaryNode(1, None, BinaryNode(2))
print(isSameTree(t1, t2))
print(isSameTree(t2, t3))
print(isSameTree(t4, t5))
print(isSameTreeV2(t1, t2))
print(isSameTreeV2(t2, t3))
print(isSameTreeV2(t4, t5))