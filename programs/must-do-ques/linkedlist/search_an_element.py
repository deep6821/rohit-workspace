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
            new_node.nexxt = self.start
            self.start = new_node
            return

        temp = self.start
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def display_ll(self):
        temp = self.start
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def search_an_element(self, x):
        if self.start is None:
            return

        temp = self.start
        while temp:
            if temp.data == x:
                print("Data found")
                return True
            else:
                temp = temp.next
        return False


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.insert_at_end(40)
    ll.insert_at_end(50)
    ll.display_ll()
