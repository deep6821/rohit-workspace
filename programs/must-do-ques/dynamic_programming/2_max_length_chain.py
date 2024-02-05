"""
Maximum Length Chain of Pairs:
You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.
A pair (c, d) can follow another pair (a, b) if b < c. Chain of pairs can be formed in this fashion. Find the
longest chain which can be formed from a given set of pairs.

For example, if the given pairs are {{5, 24}, {39, 60}, {15, 28}, {27, 40}, {50, 90} }, then the longest chain
that can be formed is of length 3, and the chain is {{5, 24}, {27, 40}, {50, 90}}
"""

class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b


def max_chain_length(arr, n):
    # Initialize MCL(max chain length) values for all indices
    mcl = [1 for i in range(n)]

    # Compute optimized chain length values in bottom up manner
    for i in range(1, n):
        for j in range(0, i):
            if arr[i].a > arr[j].b and mcl[i] < mcl[j] + 1:
                mcl[i] = mcl[j] + 1

    # # Pick maximum of all MCL values
    # for i in range(n):
    #     if (max < mcl[i]):
    #         max = mcl[i]
    #
    # return max
    return max(mcl)


arr = [Pair(5, 24), Pair(15, 25), Pair(27, 40), Pair(50, 60)]
print(max_chain_length(arr, len(arr)))
