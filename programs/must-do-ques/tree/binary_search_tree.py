class BinarySearchTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)


def insert_node(root, key):
    new_node = BinarySearchTree(key)
    if root is None:
        root = new_node
    else:
        if new_node.key < root.key:
            if root.left is None:
                root.left = new_node
            else:
                insert_node(root.left, key)
        else:
            if root.right is None:
                root.right = new_node
            else:
                insert_node(root.right, key)


def minimum_node_value(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def delete_node(root, key):
    if root is None:
        return root

    if key < root.key:
        root.left = delete_node(root.left, key)

    elif key > root.key:
        root.right = delete_node(root.right, key)

    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = minimum_node_value(root.right)
        root.key = temp.key
        root.right = delete_node(root.right, temp.key)

    return root


def search(root, key):
    if root is None or root.key == key:
        return root

    if key < root.key:
        return search(root.left, key)
    return search(root.right, key)


if __name__ == "__main__":
    root = BinarySearchTree(50)
    insert_node(root, 30)
    insert_node(root, 20)
    insert_node(root, 40)
    insert_node(root, 70)
    insert_node(root, 60)
    insert_node(root, 80)
    inorder(root)
    print("\n++++++++++++++++++++++++++++++++++++++++++++++")
    deleted_node = delete_node(root, 20)
    # print("deleted_node: {}".format(deleted_node.key))
    # print("\n++++++++++++++++++++++++++++++++++++++++++++++")
    inorder(root)
