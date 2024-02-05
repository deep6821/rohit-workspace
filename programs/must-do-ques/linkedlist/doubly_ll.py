class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.start = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.start
        if self.start is not None:
            self.start.prev = None
        self.start = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start is None:
            new_node.prev = None
            self.start = new_node
            return

        temp = self.start
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp
        return

    def insert_at_after_given_node(self, prev_node, data):
        if prev_node is None:
            print("the given previous node cannot be NULL")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next is not None:
            new_node.next.prev = new_node
