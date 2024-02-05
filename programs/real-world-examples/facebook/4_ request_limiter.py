"""
Time complexity:
----------------
The time complexity is O(1) because the program runs at a constant time complexity.

Space complexity:
-----------------
The space complexity is O(R), where R is the size of incoming requests that we store.
"""


class request_limiter:
    def __init__(self):
        self.requests = {}

    def request_approver(self, timestamp, request):
        # Returns true if the message should be printed in the given timestamp,
        # otherwise returns false.

        if request not in self.requests or timestamp - self.requests[request] >= 5:
            self.requests[request] = timestamp
            print("Request Accepted")
            return True
        else:
            print("Request Rejected")
            return False


# Driver code

obj = request_limiter()
obj.request_approver(1, "send_message")
obj.request_approver(2, "block")
obj.request_approver(3, "send_message")
obj.request_approver(8, "block")
obj.request_approver(10, "send_message")
obj.request_approver(11, "send_message")