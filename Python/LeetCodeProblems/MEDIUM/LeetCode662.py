# LEET CODE 662 Maximum Width of Binary Tree
# given the root of a binary tree, return the maximum
# width of the tree.
from BinaryTree import BinaryNode
def widthOfBinaryTree(root):
    nodes = []

    def getNodeWeight(node):
        if not node.left and not node.right:
            return 1
        elif node.left and node.right:
            return 1 + getNodeWeight(node.left) + getNodeWeight(node.right)
        elif node.left:
            return 1 + getNodeWeight(node.left)
        elif node.right:
            return 1 + getNodeWeight(node.right)
    
    def helper(node):
        if node != None:
            nodes.append([node.val, getNodeWeight(node) - 1])
            helper(node.left)
            helper(node.right)
        else:
            return
        
    helper(root)
    return nodes


tree = BinaryNode(1, BinaryNode(3, BinaryNode(5), BinaryNode(3)), BinaryNode(2, None, BinaryNode(9)))
tree2 = BinaryNode(1, BinaryNode(3, BinaryNode(5), None), BinaryNode(2, None, None))
tree3 = BinaryNode(1,BinaryNode(3,BinaryNode(5), BinaryNode(3)), None)
print(widthOfBinaryTree(tree))
print(widthOfBinaryTree(tree2))
print(widthOfBinaryTree(tree3))

