"""
Given a Binary Tree, find the maximum(or minimum) element in it. For example, maximum in the following Binary
Tree is 9.

In Binary Search Tree, we can find maximum by traversing right pointers until we reach the rightmost node.
But in Binary Tree, we must visit every node to figure out maximum. So the idea is to traverse the given
tree and for every node return maximum of 3 values.

1) Node’s data.
2) Maximum in node’s left subtree.
3) Maximum in node’s right subtree.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def find_max(root):
    # Base case
    if root is None:
        return float('-inf')

    # Return maximum of 3 values:  1) Root's data. 2) Max in Left Subtree. 3) Max in right subtree
    res = root.data
    lres = find_max(root.left)
    rres = find_max(root.right)
    if lres > res:
        res = lres
    if rres > res:
        res = rres
    return res


def find_min(root):
    if root is None:
        return float('inf')
    res = root.data
    lres = find_min(root.leftChild)
    rres = find_min(root.rightChild)
    if lres < res:
        res = lres
    if rres < res:
        res = rres
    return res


# Driver Code
if __name__ == '__main__':
    root = Node(2)
    root.left = Node(7)
    root.right = Node(5)
    root.left.right = Node(6)
    root.left.right.left = Node(1)
    root.left.right.right = Node(11)
    root.right.right = Node(9)
    root.right.right.left = Node(4)
    print("Maximum element is", find_max(root))
