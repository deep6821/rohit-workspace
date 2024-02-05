"""
Implement a function that connects n pipes of different lengths, into one pipe.
You can assume that the cost to connect two pipes is equal to the sum of their
lengths. We need to connect the pipes with minimum cost.

Input:
------
A list containing lengths of n pipes

Output:
-------
The total cost of connecting the pipes

Sample input
pipes = [4, 3, 2, 6]
Sample output
result = 29

Solution: sorting

Explanation:
------------
If you look at the animation present in the previous lesson, you will notice
that the lengths of the pipes which are picked first are included iteratively
(i.e. each time). Therefore, we want them to be as small as possible.

First, we sort the lengths of the pipes. This ensures that the smallest length
pipe is selected in the first iteration. Then, we add its length to the next
largest pipe which is in the sorted list. In this way, in every iteration,
the previous cost (which is the length of the last two pipes connected) is
added to the length of the next pipe until all pipes are connected.

Time complexity:
----------------
The time complexity for this solution is O(nlogn), because of the use of the
optimized built-in Python sort function also known as Timsort.
"""


def min_cost(pipes):
    """
    Calculates the minimum cost of connecting pipes
    :param pipes: A list where its length is the number of pipes and indexes are the specific lengths of the pipes.
    :return: The minimum cost
    """

    cost = 0
    n = len(pipes)

    pipes.sort()  # Sorting the list using the .sort() built-in function

    for i in range(n - 1):
        prev_cost = cost  # store previous cost for later use

        cost = (pipes[i] + pipes[i + 1])  # find current cost
        pipes[i + 1] = cost  # insert in list

        cost = cost + prev_cost  # add with previous cost

    return cost


# Main program to test above function
if __name__ == "__main__":
    pipes = [4, 3, 2, 6]

    print(min_cost(pipes))
