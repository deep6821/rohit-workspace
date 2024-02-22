class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)

    def is_empty(self):
        return len(self.queue) == 0

    def dequeue(self):
        if not self.is_empty:
            return self.queue.pop(0)
        else:
            return "Queue is underflow | empty"

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is underflow | empty"
        
class Queue1:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size
    
    def is_full(self):
        return len(self.queue) == self.max_size

    def enqueue(self, item):
        if not self.is_full():
            return self.queue.append(item)
        else: 
            return("Queue is overflow | full")

    def is_empty(self):
        return len(self.queue) == 0

    def dequeue(self):
        if not self.is_empty:
            return self.queue.pop(0)
        else:
            return "Queue is underflow | empty"

    def peek(self):
        if not self.is_empty:
            return self.queue[0]
        else:
            return "Queue is underflow | empty"
    
class Queue2:
    def __init__(self):
        self.queue = []
        self.front = -1
        self.rear = -1

    def size(self):
        if self.is_empty():
            return 0
        else:
            return self.rear - self.front + 1
        
    def is_full(self):
        return (self.rear + 1) % self.max_size == self.front
    
    def is_empty(self):
        return self.front == -1

    def enqueue(self, item):
        if self.is_empty():
            self.front, self.rear = 0, 0
        else:
            self.rear +=1
        
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            front_item = self.queue[self.front]
            if self.front == self.rear:
                self.front, self.rear = -1, -1
            else:
                self.front +=1
            return front_item
        else:
            return "Queue is underflow | empty"

    def peek(self):
        if not self.is_empty():
            return self.items[self.front]
        else:
            return "Queue is underflow | empty"


if __name__ == "__main__":
    cls_obj = Queue1(4)
    cls_obj.enqueue(1)
    cls_obj.enqueue(2)
    cls_obj.enqueue(3)
    cls_obj.enqueue(4)
    cls_obj.enqueue(5)
    cls_obj.dequeue()

    print(cls_obj.queue)
    print( cls_obj.peek())
