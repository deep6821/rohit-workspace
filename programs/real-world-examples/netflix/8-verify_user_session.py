"""
Let n be the size of the pushed (or popped) stack.

Time complexity:
----------------
The time complexity will be O(n) because n elements will be pushed, and n elements will get popped.

Space complexity:
-----------------
In the worst case, all n elements will be pushed into the stack, so the space complexity will be O(n).
"""


def verify_session(push_op, pop_op):
    if len(push_op) != len(pop_op):
        return False
    i = 0
    stack = []
    for pid in push_op:
        stack.append(pid)
        while stack and stack[-1] == pop_op[i]:
            stack.pop()
            i += 1

    if not stack:
        return True
    return False


# Driver code
push_op = [1, 2, 3, 4, 5]
pop_op = [5, 4, 3, 2, 1]

if verify_session(push_op, pop_op):
    print("Session Successfull!")
else:
    print("Session Faulty!")
