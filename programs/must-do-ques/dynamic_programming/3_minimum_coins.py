"""
Given a value N, total sum you have. You have to make change for Rs. N, and there is infinite supply of each of
the denominations in Indian currency, i.e., you have infinite supply of { 1, 2, 5, 10, 20, 50, 100, 200, 500, 2000}
valued coins/notes, Find the minimum number of coins and/or notes needed to make the change for Rs N.

Input: coins[] = {25, 10, 5}, V = 30
Output: Minimum 2 coins required
We can use one coin of 25 cents and one of 5 cents.
"""
import sys


# Time complexity of the above solution is O(mv).
# m is size of coins array (number of different coins)
def minimum_coins(coins, m, V):
    # table[i] will be storing the minimum number of coins required for i value.
    # so table[V] will have result
    table = [0 for i in range(V + 1)]

    # Base case (If given value V is 0)
    table[0] = 0

    # Initialize all table values as Infinite
    for i in range(1, V + 1):
        table[i] = sys.maxsize

    # Compute minimum coins required for all values from 1 to V
    for i in range(1, V + 1):

        # Go through all coins smaller than i
        for j in range(m):
            if coins[j] <= i:
                sub_res = table[i - coins[j]]
                if (sub_res != sys.maxsize and
                        sub_res + 1 < table[i]):
                    table[i] = sub_res + 1
    return table[V]


# Driver Code
if __name__ == "__main__":
    coins = [9, 6, 5, 1]
    m = len(coins)
    V = 11
    print("Minimum coins required is: ", minimum_coins(coins, m, V))



