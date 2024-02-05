class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.start = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start is None:
            self.start = new_node
            return

        temp = self.start
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def find_length_iterative(self):
        if self.start is None:
            return

        count = 0
        temp = self.start
        while temp:
            count += 1
            temp = temp.next
        return count

    def find_length_rec(self, temp):
        if not temp:
            return 0
        else:
            return 1 + self.find_length_rec(temp.next)

    def find_length_recursive(self):
        temp_node = self.start
        return self.find_length_rec(temp_node)

    def display_ll(self):
        temp = self.start
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.insert_at_end(40)
    ll.insert_at_end(50)
    print("Print linked list: ")
    ll.display_ll()

    print("\nPrint length of linked list iterative: ",  ll.find_length_iterative())
    print("\nPrint length of linked list recursive: ", ll.find_length_recursive())

