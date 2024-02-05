class Queue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # Method 1 (By making enQueue operation costly)

    # Here time complexity will be O(n)
    def en_queue1(self, item):
        # Move all elements from stack1 to stack2
        while len(self.stack1) != 0:
            self.stack2.append(self.stack1[-1])
            self.stack1.pop()

        self.stack1.append(item)

        # Push everything back to stack1
        while len(self.stack2) != 0:
            self.stack1.append(self.stack2[-1])
            self.stack2.pop()

    # Here time complexity will be O(1)
    def de_queue1(self):
        # If the stack1 is empty
        if len(self.stack1) == 0:
            print("Queue is empty")

        popped_item = self.stack1.pop()
        return popped_item

    # Method 2 (By making deQueue operation costly)

    # Here time complexity will be O(1)
    def en_queue2(self, item):
        self.stack1.append(item)

    # Here time complexity will be O(n)
    def de_queue2(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            print("Error")

        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop(0))
                popped_item = self.stack2.pop()
                return popped_item


queue = Queue()
# queue.en_queue1(10)
# queue.en_queue1(20)
# queue.en_queue1(30)
#
# print(queue.de_queue1())

queue.en_queue2(10)
queue.en_queue2(20)
queue.en_queue2(30)

print(queue.de_queue2())
print(queue.de_queue2())
