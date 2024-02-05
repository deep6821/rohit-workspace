"""
Minimum cost to reach a point N from 0 with two different operations allowed

Given integers N, P and Q where N denotes the destination position. The task is to move from position 0 to position N
with minimum cost possible and print the calculated cost.

All valid movements are:
From position X you can go to position X + 1 with a cost of P
Or, you can go to the position 2 * X with a cost of Q

Input: N = 1, P = 3, Q = 4
Output: 3

Move from position 0 to 1st position with cost = 3.
"""


def minimum_cost(n, p, q):
    cost = 0
    while n > 1:
        if int(n) & 1:
            cost += p
            n -= 1
        else:
            temp = n / 2
            if temp * p > q:
                cost += q
            else:
                cost += p * temp
            n /= 2

    print(cost)


minimum_cost(9, 5, 1)
