"""
This is complete program for create and delete the linked list
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.start = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.start
        self.start = new_node

    def insert_at_end(self, new_data):
        new_node = Node(new_data)
        if self.start is None:
            self.start = new_node
            return

        temp = self.start
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_at_after_given_node(self, prev_node, data):
        # 1. check if the given prev_node exists
        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return

        #  2. Create new node & Put in the data
        new_node = Node(data)
        # 3. Make next of new Node as next of prev_node
        new_node.next = prev_node.next
        # 4. make next of prev_node as new_node
        prev_node.next = new_node

    def insert_at_any_position(self, data, pos):
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

    def delete_at_beginning(self):
        if self.start is None:
            return

        temp = self.start
        self.start = temp.next
        del temp

    def delete_a_given_key(self, node):
        temp = self.start
        # If head node itself holds the key to be deleted
        if temp is not None:
            if temp.data == node:
                self.start = temp.next
                temp = None
                return

        # Search for the key to be deleted, keep track of the  previous node as we need to change 'prev.next'
        while temp is not None:
            if temp.data == node:
                break
            prev_node = temp
            temp = temp.next

        # if key was not present in linked list
        if temp is None:
            return

        # Unlink the node from linked list
        prev_node.next = temp.next
        temp = None

    def delete_at_any_position(self, pos):
        # If linked list is empty
        if self.start is None:
            return

        temp = self.start
        # If start  needs to be removed
        if pos == 0:
            self.start = temp.next
            temp = None
            return

        # Find previous node of the node to be deleted
        for i in range(pos - 1):
            temp = temp.next
            if temp is None:
                break

        # If position is more than number of nodes
        if temp is None:
            return

        if temp.next is None:
            return

        # Node temp.next is the node to be deleted store pointer to the temp1 of node to be deleted
        temp1 = temp.next.next

        # Unlink the node from linked list
        temp.next = None

        temp.next = temp1

    def delete_at_end(self):
        if self.start is None:
            return

        temp = self.start
        while temp.next.next:
            temp = temp.next

        temp.next = None

    def delete_ll(self):
        temp = self.start
        while temp:
            prev = temp.next
            # delete the current node
            del temp.data
            # set current equals prev node
            temp = prev

    def display_list(self):
        temp = self.start
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


if __name__ == "__main__":
    ll = LinkedList()

    print("Insert at beginning: ")
    # ll.add_node_at_beginning(10)
    # ll.add_node_at_beginning(20)
    # ll.add_node_at_beginning(30)
    # ll.add_node_at_beginning(40)
    # ll.add_node_at_beginning(50)

    print("\nInsert at end: ")
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.insert_at_end(40)
    ll.insert_at_end(50)
    ll.insert_at_beginning(5)
    ll.display_list()

    print("\nInsert at after given node: ")
    ll.insert_at_after_given_node(ll.start.next.next, 15)
    ll.display_list()

    print("\nInsert at any postion: ")
    ll.insert_at_any_position(25, 2)
    ll.display_list()

    print("\nDelete at any beginning: ")
    ll.delete_at_beginning()
    ll.display_list()

    print("\nDelete at end: ")
    ll.delete_at_end()
    ll.display_list()

    print("\nDelete at end: ")
    ll.delete_a_given_node(30)
    ll.display_list()

    print("\nDelete at any position: ")
    ll.delete_at_any_position(2)
    ll.display_list()

    # delete linked list
    print("\nDelete linked list: ")
    ll.delete_ll()
    ll.display_list()
