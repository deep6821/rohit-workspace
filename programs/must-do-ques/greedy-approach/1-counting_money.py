"""
Given an infinite number of quarters (25 cents), dimes (10 cents),
nickels (5 cents), and pennies (1 cent)(1cent), implement a function to
calculate the minimum number of coins to represent v cents.

Input:
------
A variable v (total money to convert to coins) and a list of available coins

Output:
-------
The minimum number of coins among the available coins that add up to the
original number v, i.e., the coins represent v cents

Sample Input:
-------------
v = 19
available_coins = [1, 5, 10, 25]

Sample Output:
result = [10, 5, 1, 1, 1, 1]


Explanation:
------------
The simple greedy idea is to start from the largest possible coin available and
keep adding coins, while the remaining value is greater than 0.

The problem can be easily solved by The Greedy Method. Simply grab the largest
coin that does not cause a negative number when it’s subtracted from the
remaining total.

Time complexity:
----------------
Since there is a nested loop, i.e., the while loop inside a for loop, the time
complexity is O(n^2)
​
"""


def find_min_coins(v, coins_available):
    """
    This function finds the minimum number of coins
    :param v: Total amount
    :param coins_available: Coins available in the machine
    :return: A list of total coins
    """

    # Initialize result
    result = []
    n = len(coins_available)

    # Traverse through all available coins
    for i in reversed(range(n)):
        while v >= coins_available[i]:
            v -= coins_available[i]
            result.append(coins_available[i])

    return result


# Main program to test the above code
if __name__ == "__main__":
    coins_available = [1, 5, 10,
                       25]  # The available coins are in increasing order
    print(find_min_coins(19, coins_available))
