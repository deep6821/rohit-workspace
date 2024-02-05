"""
Count Triplets such that one of the numbers can be written as sum of the other two

Input : A[] = {1, 2, 3, 4, 5}
Output : 4
The valid triplets are:
(1, 2, 3), (1, 3, 4), (1, 4, 5), (2, 3, 5)

This is a counting problem. Lets say f(x) represents the frequency of number x in our array.
There exist four cases:

All three numbers are equal to 0. The number of ways = f(0)C3 (where pCq is the number of ways of choosing q numbers from p numbers).
One number is equal to 0, the other two are equal to some x > 0: f(0) * f(x)C2.
Two numbers are equal to some x>0, the third is 2*x: f(x)C2 * f(2 * x).
The three numbers are x, y and x + y, 0 < x, y: f(x) * f(y) * f(x + y).

"""


def count_ways(arr, n):
    # compute the max value in the array  and create frequency array of size max_val + 1.
    # We can also use HashMap to store frequencies. We have used an array  to keep remaining code simple.
    max_val = 0
    for i in range(n):
        max_val = max(max_val, arr[i])

    freq = [0 for i in range(max_val + 1)]

    for i in range(n):
        freq[arr[i]] += 1

    ans = 0  # stores the number of ways

    # Case 1: 0, 0, 0
    ans += (freq[0] * (freq[0] - 1) *
            (freq[0] - 2) // 6)

    # Case 2: 0, x, x
    for i in range(1, max_val + 1):
        ans += (freq[0] * freq[i] *
                (freq[i] - 1) // 2)

    # Case 3: x, x, 2*x
    for i in range(1, (max_val + 1) // 2):
        ans += (freq[i] *
                (freq[i] - 1) // 2 * freq[2 * i])

    # Case 4: x, y, x + y
    # iterate through all pairs (x, y)
    for i in range(1, max_val + 1):
        for j in range(i + 1, max_val - i + 1):
            ans += freq[i] * freq[j] * freq[i + j]

    return ans


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    print(count_ways(arr, n))
