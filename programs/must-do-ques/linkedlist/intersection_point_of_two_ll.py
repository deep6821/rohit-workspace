"""
Write a function to get the intersection point of two Linked Lists:
-------------------------------------------------------------------

There are two singly linked lists in a system. By some programming error, the end node of one of the linked list
got linked to the second list, forming an inverted Y shaped list.  Write a program to get the point where two linked
list merge.

Time Complexity: O(m+n)
Auxiliary Space: O(1)

Algorithm:
1. Get count of the nodes in the first list, let count be c1.
2. Get count of the nodes in the second list, let count be c2.
3. Get the difference of counts d = abs(c1 - c2)
4. Now traverse the bigger list from the first node till d nodes so that from here onwards both the lists have
equal no of nodes.  Then we can traverse both the lists in parallel till we come across a common node
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.start1 = None
        self.start2 = None

    def get_merge_node(self, d, start1, start2):
        first = start1
        second = start2

        for i in range(0, d):
            if first is None:
                return -1
            first = first.next

        while first is not None and second is not None:
            if first.data == second.data:
                return first.data

            first = first.next
            second = second.next

        return -1

    def get_length(self, start):
        count = 0
        temp = start
        while temp:
            count += 1
            temp = temp.next
        return count

    def get_node(self):
        l1 = self.get_length(self.start1)
        l2 = self.get_length(self.start2)

        if l1 > l2:
            d = l1 - l2
            return self.get_merge_node(d, self.start1, self.start2)
        else:
            d = l2 - l1
            return self.get_merge_node(d, self.start2, self.start1)


if __name__ == "__main__":
    ll = LinkedList()
    ll.start1 = Node(3)
    ll.start1.next = Node(6)
    ll.start1.next.next = Node(9)
    ll.start1.next.next.next = Node(15)
    ll.start1.next.next.next.next = Node(30)

    ll.start2 = Node(10)
    ll.start2.next = Node(15)
    ll.start2.next.next = Node(30)

    print(ll.get_node())
