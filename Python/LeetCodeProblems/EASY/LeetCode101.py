# LEET CODE 101 Symmetric Tree
# Given the root of a binary, check whether it is a 
# mirror of itself . . . 
from BinaryTree import BinaryNode

def isSymmetric(root): # solution one
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
    if root != None:
        tree1 = process(root.left)
        tree2 = process(root.right)
        print(tree1)
        print(tree2)
        return tree1 != tree2


tree = BinaryNode(1, BinaryNode(2,BinaryNode(3),BinaryNode(4)), BinaryNode(2,BinaryNode(4),BinaryNode(3)))
print(isSymmetric(tree))
tree2 = BinaryNode(1,BinaryNode(2,None,BinaryNode(3)), BinaryNode(2,None,BinaryNode(3)))
print(isSymmetric(tree2))