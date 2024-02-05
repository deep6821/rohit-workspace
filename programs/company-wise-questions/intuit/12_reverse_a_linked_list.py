"""
1. We are not moving data
2. We have to simply adjusts the links.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.start = None

    def insert_node_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.start
        self.start = new_node

    def reverse(self):
        prev = None
        current = self.start
        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        self.start = prev

    def print_node(self):
        temp = self.start
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_node_at_beginning(20)
    ll.insert_node_at_beginning(4)
    ll.insert_node_at_beginning(15)
    ll.insert_node_at_beginning(85)
    print("Given Linked List: ")
    ll.print_node()
    ll.reverse()
    print("\nReversed Linked List: ")
    ll.print_node()
