"""
Time complexity:
----------------
In the push() operation, we are setting one element in the stack, so the time complexity will be O(1).
In the pop() operation, we are removing one element, so the time complexity will also be O(1).
Additionally, the max_rating function only fetches the top element of the max stack, it will be O(1) as well.

Space complexity:
----------------
In the worst case, all operations would be push on the two stacks, and O(n) space will be utilized.


What if you had to implement an efficient min stack, meaning a stack from which you can access the smallest element in
constant time? Think about how your implementation would change?
"""
from stack import Stack


class MaxStack:
    # Constructor
    def __init__(self):
        self.max_stack = Stack()
        self.main_stack = Stack()
        return

        # Removes and returns value from max_stack

    def pop(self):
        self.max_stack.pop()
        return self.main_stack.pop()

        # Pushes values into max_stack

    def push(self, value):
        self.main_stack.push(value)
        if self.max_stack.is_empty() or self.max_stack.top() < value:
            self.max_stack.push(value)
        else:
            self.max_stack.push(self.max_stack.top())

        # Returns maximum value from newStack in O(1) Time

    def max_rating(self):
        if not self.max_stack.is_empty():
            return self.max_stack.top()


ratings = MaxStack()
ratings.push(5)
ratings.push(0)
ratings.push(2)
ratings.push(4)
ratings.push(6)
ratings.push(3)
ratings.push(10)

print(ratings.main_stack.stack_list)
print("Maximum Rating: " + str(ratings.max_rating()))

ratings.pop()  # Back button effect
print("\nAfter clicking back button\n")
print(ratings.main_stack.stack_list)
print("Maximum value: " + str(ratings.max_rating()))
