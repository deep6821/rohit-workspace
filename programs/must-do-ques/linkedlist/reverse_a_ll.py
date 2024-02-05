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
            print("", temp.data, end=" ")
            temp = temp.next

    def reverse_a_list(self):
        current_ptr = self.head
        prev_ptr = None
        next_ptr = None
        while current_ptr:
            next_ptr = current_ptr.next
            current_ptr.next = prev_ptr
            prev_ptr = current_ptr
            current_ptr = next_ptr

        self.head = prev_ptr

    def reverse(self, curr_ptr, prev_ptr):
        if curr_ptr.next is None:
            self.head = curr_ptr
            curr_ptr.next = prev_ptr
            return

        temp_ptr = curr_ptr.next
        curr_ptr.next = prev_ptr
        self.reverse(curr_ptr=temp_ptr, prev_ptr=curr_ptr)

    def reverse_a_list_using_two_ptr1(self):
        if self.head is None:
            return
        self.reverse(curr_ptr=self.head, prev_ptr=None)

    def reverse_a_list_using_two_ptr2(self):
        curr_ptr = self.head
        prev_ptr = None
        while curr_ptr:
            temp_ptr, curr_ptr.next = curr_ptr.next, prev_ptr
            prev_ptr, curr_ptr = curr_ptr, temp_ptr

        self.head = prev_ptr


if __name__ == "__main__":
    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.push(4)
    ll.push(5)
    ll.push(6)
    ll.print_list()
    ll.reverse_a_list()
    print("\n++++++++++++++++++++++++++++++++++")
    ll.print_list()
