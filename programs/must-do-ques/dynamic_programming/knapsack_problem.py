"""
Given two integer lists that represent the weights and profits of N items,
implement a function knap_sack() that finds a subset of these items which will
give us the maximum profit, so that their cumulative weight is not more than a
given number capacity. Each item can only be selected once, which means we
either skip it or put it in the knapsack.

Inputs:
   profits = [60, 100, 120]
   weights = [10, 20, 30]
   capacity = 50

Output: 220

Explanation:
Weight          Profit Value
10              60  -> 70
20              100 -> 120
30              120 -> 150
10, 20          60, 100 -> 160
10, 30          60, 120 -> 180
20, 30          100, 120 -> 220(max profit)
30, 20, 10 > 50
"""


def knap_sack(profits, weights, capacity):
    profit_length = len(profits)
    # Base condition
    if capacity <= 0 or profit_length == 0:
        return 0

    lookup_table = [0] * (capacity + 1)
    # if only single weight
    for i in range(0, capacity + 1):
        if weights[0] <= i:
            lookup_table[i] = profits[0]

    print("lookup_table: ", lookup_table)
    for i in range(1, profit_length):
        # print(i)
        for j in reversed(range(0, capacity + 1)):
            # print(j)
            p1, p2 = 0, 0
            if weights[i] <= j:
                # print("here -")
                p1 = profits[i] + lookup_table[j - weights[i]]
                # print(p1)
            p2 = lookup_table[j]
            # print(p2)
            lookup_table[j] = max(p1, p2)

    print("lookup_table: ", lookup_table)
    return lookup_table[capacity]


if __name__ == "__main__":
    profits = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50
    max_profit = knap_sack(profits, weights, capacity)
    print(max_profit)
