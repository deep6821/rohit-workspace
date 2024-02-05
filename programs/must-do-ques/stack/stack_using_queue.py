# from queue import Queue
#
#
# class Stack(object):
#     def __init__(self):
#         self.size = 0
#         self.q1 = Queue()
#         self.q2 = Queue()
#
#     def push(self, item):
#         # Push item, first in empty q2
#         self.q2.put(item)
#
#         # Push all the remaining elements in q1 to q2
#         while not self.q1.empty():
#             self.q2.put(self.q1.queue[0])
#             self.q1.get()
#
#
# stack = Stack()
# stack.push(10)


class Queue(object):
    def __init__(self):
        self.items = []

    def is_full(self):
        pass

    def is_empty(self):
        return self.items == []

    def en_queue(self, item):
        self.items.append(item)

    def de_queue(self):
        return self.items.pop(0)

    def peek(self):
        return len(self.items) - 1


class Stack(object):
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def is_full(self):
        self.queue2.is_full()

    def is_empty(self):
        self.queue2.is_empty()

    def push(self, item):
        self.queue1.en_queue(item)
        while not self.queue2.is_empty():
            x = self.queue2.de_queue()
            self.queue1.en_queue(x)

        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        return self.queue2.de_queue()

    def peek(self):
        pass



s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)

print(s.pop())
