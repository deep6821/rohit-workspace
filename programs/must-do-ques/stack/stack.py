class Stack(object):
    def __init__(self, size=5):
        self.stack = []
        self.size = size

    def is_full(self):
        if len(self.stack) >= self.size:
            return False
        return True

    def is_empty(self):
        if len(self.stack) <= 0:
            return False
        return True

    def push(self, item):
        if self.is_full():
            self.stack.append(item)
            print(str(item) + " pushed to stack ")
        else:
            print("Stack is Overflow/Full")

    def pop(self):
        if self.is_empty():
            popped_item = self.stack.pop()
            print(str(popped_item) + " popped from stack")
        else:
            print("Stack is Underflow/Empty")

    def peek(self):
        return len(self.stack) - 1


class LinkedList(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class StackUsingLL(object):
    def __init__(self):
        self.head = None

    def is_full(self):
        """ Not valid while creating Stack using LinkedList"""
        pass

    def is_empty(self):
        # return True if self.head is None else False
        pass

    def push(self, item):
        new_node = LinkedList(item)
        new_node.next = self.head
        self.head = new_node
        print(str(item) + " pushed to stack ")

    def pop(self):
        if self.head is None:
            return

        temp = self.head
        self.head = self.head.next
        popped_item = temp.data
        print(str(popped_item) + " popped from stack")

    def peek(self):
        return self.head.data


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
# stack.push(60)  # Stack is Overflow/Full

print("\n+++++++++++++++++++++++++++++++")
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
# stack.pop()  # Stack is Underflow/Empty
