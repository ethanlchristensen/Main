# LEET CODE 872 Leaf Similar Trees
# given two root nodes of binary trees return whether or not
# they are leaf similar. Trees are leaf similar if they a) have
# the same leaves and b) they occur in the smame order.
from BinaryTree import BinaryNode

def leafSimilar(root1, root2):
    def process(node):
        res = []
        def helper(node):
            if node != None:
                if node.left == None and node.right == None:
                    res.append(node.val)
                    return
                else:
                    helper(node.left)
                    helper(node.right)
        helper(node)
        return res
    
    return process(root1) == process(root2)


tree1 = BinaryNode(3, BinaryNode(5, BinaryNode(6), BinaryNode(2, BinaryNode(7), BinaryNode(4))), BinaryNode(1, BinaryNode(9), BinaryNode(8)))
tree2 = BinaryNode(3, BinaryNode(5, BinaryNode(6), BinaryNode(7)), BinaryNode(1, BinaryNode(4), BinaryNode(2, BinaryNode(9), BinaryNode(8))))
print(leafSimilar(tree1, tree2))
tree3 = BinaryNode(1, BinaryNode(2), BinaryNode(3))
tree4 = BinaryNode(1, BinaryNode(3), BinaryNode(2))
print(leafSimilar(tree3, tree4))