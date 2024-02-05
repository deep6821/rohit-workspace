class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.start = None

    def add_node_at_beginning(self, data):
        new_node = Node(data)
        if self.start is None:
            new_node.next = self.start
            self.start = new_node
            return
        else:
            new_node.next = self.start
            self.start = new_node

    def add_node_at_end(self, data):
        new_node = Node(data)
        if self.start is None:
            new_node.next = self.start
            self.start = new_node
            return
        else:
            temp = self.start
            while temp.next:
                temp = temp.next

            temp.next = new_node

    def add_node_at_any_position(self, data, pos):
        new_node = Node(data)
        if self.start is None or pos == 0:
            new_node.next = self.start
            self.start = new_node
            return
        else:
            temp = self.start
            while pos - 1 > 0:
                if temp.next is not None:
                    temp = temp.next
                    pos -= 1
                else:
                    break

            new_node.next = temp.next
            temp.next = new_node

    def add_node_at_given_node(self, prev_node, data):
        new_node = Node(data)
        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return

        # Make next of new Node as next of prev_node
        new_node.next = prev_node.next
        # Make next of prev_node as new_node
        prev_node.next = new_node

    def delete_at_beginning(self):
        if self.start is None:
            return

        temp = self.start
        self.start = temp.next
        del temp

    def delete_at_end(self):
        if self.start is None:
            return

        temp = self.start
        while temp.next.next:
            temp = temp.next

        temp.next = None

    def display_linked_list(self):
        temp = self.start
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


if __name__ == "__main__":
    ll = LinkedList()
    # ll.add_node_at_beginning(10)
    # ll.add_node_at_beginning(20)
    # ll.add_node_at_beginning(30)
    # ll.add_node_at_beginning(40)
    # ll.add_node_at_beginning(50)

    ll.add_node_at_end(10)
    ll.add_node_at_end(20)
    ll.add_node_at_end(30)
    ll.add_node_at_end(40)
    ll.add_node_at_end(50)

    ll.add_node_at_any_position(35, 3)

    ll.add_node_at_given_node(ll.start.next, 25)

    ll.delete_at_beginning()

    ll.delete_at_end()

    ll.display_linked_list()
