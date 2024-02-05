class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def find_middle_element(self):
        slow_ptr = self.head
        fast_ptr = self.head

        if self.head is not None:
            while fast_ptr and fast_ptr.next:
                slow_ptr = slow_ptr.next
                fast_ptr = fast_ptr.next.next

        print("\nThe middle element is: {}".format(slow_ptr.data))


if __name__ == "__main__":
    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.push(4)
    ll.push(5)
    ll.push(6)
    ll.print_list()
    ll.find_middle_element()

