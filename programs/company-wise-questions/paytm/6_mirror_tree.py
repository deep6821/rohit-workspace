class Tree:
    def __init__(self, data):
        self.data = data
        self.left, self.right = None


def mirror(node):
    if node is None:
        return
    else:
        temp = node
        mirror(node.left)
        mirror(node.right)

        temp = node.left
        node.left = node.right
        node.right = temp

