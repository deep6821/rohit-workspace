"""
A node is a leaf node if both left and right child nodes of it are NULL.

Here is an algorithm to get the leaf node count.
getLeafCount(node)
1) If node is NULL then return 0.
2) Else If left and right child nodes are NULL return 1.
3) Else recursively calculate leaf count of the tree using below formula.
    Leaf count of a tree = Leaf count of left subtree + Leaf count of right subtree

Time Complexity: O(n)
Auxiliary Space : If we don’t consider size of stack for function calls then O(1) otherwise O(n).
"""


class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Function to get the count of leaf nodes in binary tree
def getLeafCount(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    else:
        return getLeafCount(node.left) + getLeafCount(node.right)

    # Driver program to test above function


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Leaf count of the tree is %d" % (getLeafCount(root)))
