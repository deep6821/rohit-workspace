"""
Time complexity:
----------------
The time complexity will be O(n^2) because we traverse the complete matrix of size n^2

Space complexity:
-----------------
The space complexity is O(n) because the visited array used to store the visited users is of size n.
"""
import numpy as np


# Recursively finds all users in a single friend circle
def dfs(friends, n, visited, v):
    for x in range(n):
        # A user is in the friend circle if they are friends with the user represented by
        # user index and if they are not already in a friend circle
        if friends[v, x] and visited[x] == 0:
            if x != v:
                visited[x] = 1
                dfs(friends, n, visited, x)


def friend_circles(friends, n):
    if n == 0:
        return 0

    num_circles = 0  # Number of friend circles

    # Keep track of whether a user is already in a friend circle
    visited = np.zeros(n)

    # Start with the first user and recursively find all other users in their
    # friend circle. Then, do the same thing for the next user that is not already
    # in a friend circle. Repeat until all users are in a friend circle.
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            dfs(friends, n, visited, i)  # Recursive step to find all friends
            num_circles = num_circles + 1

    return num_circles


length = 4
arr = np.array([
    [1, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 1]
])

print("Number of friend circles:", friend_circles(arr, length))
