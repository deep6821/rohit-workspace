"""
A girl lost the key to her locker (note: The key is only numeric). She
remembers the number of digits N as well as the sum S of all the digits of her
password. She also knows that her password is the largest number of N digits
that can be possible with a given sum S.

Input #
The number of digits and the sum of those digits

Output #
The largest number that can be created (or the key) as a list

Sample input #
sum_of_digits = 20
number_of_digits = 3

Sample output #
result = [9, 9, 2]

Explanation #
We can solve the problem using the greedy approach.

The idea is to fill all digits one-by-one, from leftmost to rightmost digit
(or from most significant digit to least significant digit), then compare the
remaining sum with 9. If the remaining sum is more than 9, put 9 in the current
position; otherwise, put the remaining sum. Since we fill digits from left to
right, we put the highest digits on the left side, hence getting the largest
number.

This is a greedy approach. We use the highest number 9 and put it in the
leftmost available slot. This idea works because our problem is to find the
largest number and 9 being the largest digit, helps us do so.

This approach fails in certain conditions where the sum is less than the number
of digits or if a number is not possible in the constraints given.

Time complexity:
----------------
The time complexity is O(n)because we can simply find the solution in one
iteration.
"""


def find_largest_number(number_of_digits, sum_of_digits):
    """
    Finds the largest number with given number of digits and sum of Digits
    :param number_of_digits: Number of digits
    :param sum_of_digits: Sum of digits
    :return: Possible largest number
    """

    # If the sum of digits is 0, then a number is possible only if the number of digits is 1.
    if sum_of_digits == 0:
        if number_of_digits == 1:
            return [0]
        else:
            return [-1]

    # sum_of_digits is greater than the maximum possible sum.
    if sum_of_digits > 9 * number_of_digits:
        return [-1]

    result = [0] * number_of_digits

    # Fill from most significant digit to least significant digit!
    for i in range(number_of_digits):
        # Place 9 to make the number largest
        if sum_of_digits >= 9:
            result[i] = 9
            sum_of_digits -= 9

        # If remaining sum becomes less than 9, then fill the remaining sum
        else:
            result[i] = sum_of_digits
            sum_of_digits = 0

    return result


# Driver code to test above function
if __name__ == '__main__':
    sum_of_digits = 20
    number_of_digits = 3

    print(find_largest_number(number_of_digits, sum_of_digits))

    sum_of_digits = 100
    number_of_digits = 2

    print(find_largest_number(number_of_digits, sum_of_digits))
