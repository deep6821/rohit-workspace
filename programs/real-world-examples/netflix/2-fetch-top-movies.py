"""
Time Complexity:
----------------
The time complexity will be: O(k×n), where k is the number of the lists and n is the maximum length of a single list.

Space complexity:
----------------
O(1), as constant space was utilized.

"""
import random

print("LinkedList -------------------------------------------------------------------------------------------------")


class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        self.arbitrary = None


def insert_at_head(head, data):
    newNode = LinkedListNode(data)
    newNode.next = head
    return newNode


def insert_at_tail(head, node):
    if head is None:
        return node

    temp = head;

    while temp.next != None:
        temp = temp.next

    temp.next = node;
    return head


def create_random_list(length):
    list_head = None
    for i in range(0, length):
        list_head = insert_at_head(list_head, random.randrange(1, 100))
    return list_head


def create_linked_list(lst):
    list_head = None
    for x in reversed(lst):
        list_head = insert_at_head(list_head, x)
    return list_head


def display(head):
    temp = head
    while temp:
        print(str(temp.data), end="")
        temp = temp.next
        if temp != None:
            print(", ", end="")


def to_list(head):
    lst = []
    temp = head
    while temp:
        lst.append(temp.data)
        temp = temp.next
    return lst


def is_equal(list1, list2):
    if list1 is list2:
        return True

    while list1 != None and list2 != None:
        if list1.data != list2.data:
            return False
        list1 = list1.next
        list2 = list2.next

    return list1 == list2


print("\n ===========================================================================================================")


def merge2_country(l1, l2):  # helper function
    dummy = LinkedListNode(-1)

    prev = dummy
    while l1 and l2:
        if l1.data <= l2.data:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next
        prev = prev.next

    if l1 is not None:
        prev.next = l1
    else:
        prev.next = l2

    return dummy.next


def mergeK_county(lists):  # Main function

    if len(lists) > 0:
        res = lists[0]
        for i in range(1, len(lists)):
            res = merge2_country(res, lists[i])
        return res
    return


# Driver code
a = create_linked_list([11, 41, 51])
b = create_linked_list([21, 23, 42])
c = create_linked_list([25, 56, 66, 72])

print("All movie ID's from best to worse are:")
display(mergeK_county([a, b, c]))
