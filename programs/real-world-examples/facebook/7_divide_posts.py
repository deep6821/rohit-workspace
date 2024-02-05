"""
Let n be the size of the list of integers and m be the sum of the list elements.

Time complexity:
----------------
The binary search will take O(log(m)) time in the low and high range. Each time we pick a mid-value,
we traverse over n elements of the list, so the total time complexity will be O(n×log(m)).

Space complexity:
-----------------
The space complexity will be O(1) because constant space is utilized.
"""


def divide_posts(days, k):
    low, high = 1, sum(days) // k
    while low < high:
        mid = (low + high + 1) // 2

        # This would denote the posts we currently have
        # as we are traversing over the list
        target = 0

        # This would tell us how many days we would get after dividing
        # the list in `mid` amount of posts
        divisions = 0
        for posts in days:
            target += posts
            if target >= mid:
                divisions += 1
                target = 0
        if divisions >= k:
            low = mid
        else:
            high = mid - 1
    return high


# Driver code
days = [1000, 2000, 3000, 4000, 5000]
nodes = 3
print("The master node was assigned", divide_posts(days, nodes), "posts")
