"""
Given two numbers represented by two lists, write a function that returns the sum list.
The sum list is list representation of the addition of two input numbers.

Example:
Input: List1: 5->6->3  // represents number 365
       List2: 8->4->2 //  represents number 248
Output: Resultant list: 3->1->6  // represents number 613


Approach: Traverse both lists and One by one pick nodes of both lists and add the values. If the sum is more
than 10 then make carry as 1 and reduce sum. If one list has more elements than the other then consider remaining
values of this list as 0.

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Time Complexity: O(m + n) where m and n are number of nodes in first and second lists respectively.
    def add_two_ll_sum(self, first_list, second_list):
        prev_node = None
        temp_node = None
        carry = 0

        while first_list is not None or second_list is not None:
            first_data = 0 if first_list is None else first_list.data
            second_data = 0 if second_list is None else second_list.data
            sum = carry + first_data + second_data
            carry = 1 if sum >= 10 else 0
            sum = sum if sum < 10 else sum % 10

            temp_node = Node(sum)
            # if this is the first node then set it as head of resultant list
            if self.head is None:
                self.head = temp_node
            else:
                prev_node.next = temp_node

            prev_node = temp_node
            first_list = first_list.next if first_list else first_list
            second_list = second_list.next if second_list else second_list

        if carry > 0:
            print(carry)
            temp_node.next = Node(carry)

    def print_ll(self):
        temp = self.head
        while temp:
            print(temp.data, end="")
            temp = temp.next


if __name__ == "__main__":
    first_list = LinkedList()
    second_list = LinkedList()

    first_list.push(6)
    first_list.push(4)
    first_list.push(9)
    first_list.push(5)
    first_list.push(7)

    second_list.push(4)
    second_list.push(8)

    result = LinkedList()
    result.add_two_ll_sum(first_list.head, second_list.head)
    result.print_ll()
