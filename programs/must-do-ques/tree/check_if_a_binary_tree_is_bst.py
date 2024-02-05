"""
The idea is to use Inorder traversal and keep track of the previously visited node’s value. Since the
inorder traversal of a BST generates a sorted array as output, So, the previous element should always
be less than or equals to the current element.

While doing In-Order traversal, we can keep track of previously visited Node’s value by passing an
integer variable using reference to the recursive calls. If the value of the currently visited node is
less than the previous value, then the tree is not BST.

Time Complexity: O(N)
Auxiliary Space: O(1)
"""

import math
prev = -math.inf


class Node:
    """
    Creates a Binary tree node that has data, a pointer to it's left and right child
    """
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def checkBST(root):
    """
    Function to check if Binary Tree is a Binary Search Tree
    :param root: current root node
    :return: Boolean value
    """
    # traverse the tree in inorder fashion and update the prev node
    global prev

    if root:
        if not checkBST(root.left):
            return False

        # Handles same valued nodes
        if root.data < prev:
            return False

        # Set value of prev to current node
        prev = root.data

        return checkBST(root.right)
    return True


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(15)
    root.left.left = Node(1)
    root.left.right = Node(4)

    if checkBST(root):
        print("Is BST")
    else:
        print("Not a BST")


if __name__ == '__main__':
    main()

