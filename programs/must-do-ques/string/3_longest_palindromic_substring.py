"""
----------------------------------------------------------------------------------------------------
The time complexity of the Dynamic Programming based solution is O(n^2) and it requires O(n^2) extra
space
----------------------------------------------------------------------------------------------------

Approach:
1. The idea is to generate all even length and odd length palindromes and keep track of the longest
palindrome seen so far.
2. To generate odd length palindrome, Fix a centre and expand in both directions for longer palindromes,
i.e. fix i (index) as center and two indices as i1 = i+1 and i2 = i-1
3. Compare i1 and i2 if equal then decrease i2 and increase i1 and find the maximum length. Use a similar
technique to find the even length palindrome.
4. Take two indices i1 = i and i2 = i-1 and compare characters at i1 and i2 and find the maximum length till
all pair of compared characters are equal and store the maximum length.
5. Print the maximum length.
filter_none
"""


# TC: O(n^2) time and SC: O(1)
def longest_palsubstr(string):
    length = len(string)
    max_length, start = 1, 0
    # One by one consider every character as center point of even and length palindromes
    for i in range(1, length):
        low = i - 1
        high = i
        while low >= 0 and high < length and string[low] == string[high]:
            if high - low + 1 > max_length:
                start = low
                max_length = high - low + 1
            low -= 1
            high += 1

        # Find the longest odd length palindrome with center point as i
        low = i - 1
        high = i + 1
        while low >= 0 and high < length and string[low] == string[high]:
            if high - low + 1 > max_length:
                start = low
                max_length = high - low + 1
            low -= 1
            high += 1

    print("Longest palindrome substring is:", string[start:start + max_length])
    return max_length


string = "forgeeksskeegfor"
print("Length is: " + str(longest_palsubstr(string)))
