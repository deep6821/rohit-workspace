"""
Given three numbers x, y and p, compute (x^y) % p.

Examples :
Input:  x = 2, y = 3, p = 5
Output: 3
Explanation: 2^3 % 5 = 8 % 5 = 3.

Input:  x = 2, y = 5, p = 13
Output: 6
Explanation: 2^5 % 13 = 32 % 13 = 6.

Formulae: (ab) mod p = ( (a mod p) (b mod p) ) mod p
For example a = 50,  b = 100, p = 13
50  mod 13  = 11
100 mod 13  = 9

=> (50 * 100) mod 13 = ( (50 mod 13) * (100 mod 13) ) mod 13
=> (5000) mod 13 = ( 11 * 9 ) mod 13
=> 8 = 8
"""


# TC:  O(Log y), SC: 0(1)
def calculate_power_iterative_solution(x, y, p):
    result = 1
    x = x % p
    if x == 0:
        return 0

    while y > 0:
        # if y is odd, multiply x with result
        if y & 1 == 1:
            result = (result * x) % p

        # if y is even
        y = y >> 1  # y/2
        x = (x * x) % p
    return result


# Time Complexity: O(n)
# Space Complexity: O(1)
def calculate_power_recursive_solution(x, y):
    if y == 0:
        return 1

    elif int(y % 2) == 0:
        return (calculate_power_recursive_solution(x, int(y / 2)) * calculate_power_recursive_solution(x, int(y / 2)))

    else:
        return (x * calculate_power_recursive_solution(x, int(y / 2)) * calculate_power_recursive_solution(x, int(y / 2)))


# TC: O(logn) , SC: 0(1)
def calculate_power_dp_solution(x, y):
    if y == 0: return 1
    temp = calculate_power_dp_solution(x, int(y / 2))

    if y % 2 == 0:
        return temp * temp
    else:
        if y > 0:
            return x * temp * temp
        else:
            return (temp * temp) / x


print(calculate_power_iterative_solution(2, 5, 13))
print(calculate_power_recursive_solution(2, 3))
print(calculate_power_dp_solution(2, 3))
