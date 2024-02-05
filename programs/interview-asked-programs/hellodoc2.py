"""
String Minimization:
--------------------
You are given a string made of lowercase English latters a, b, and c.
Your task is to minimize the length of the string by applying the following operation on the string.

1. Divide the string into two non-empty parts, left and right
2. Without reversing any of the parts, swap them with each other by appending the left part of the end of
the right part.
3. While appending, if the suffix string of the right part and the prefix string of the left part contain the same
characters, then you can remove those characters from the suffix and prefix of the right and left part.
4. Repeat the third step until you do not find such prefix and suffix strings.

Determine the minimum length of the string after applying the above operations exactly once on a string.

Ex: aabcccabba
step1: left = aabcc and right = cabba
step2: appending both strings: cabbaaabcc
step3: Remove aaa from the string, now new string will be: cabbbcc
       Remove bbb from the new string -->> cacc

Input Format:
First line: s: aabcccabba

Output Format:
Print a single int denoting the minimum length of the string after applying the operations: 4
"""


def string_minimization(input_str):
    n = len(input_str)
    left = input_str[0: int(n / 2)]
    right = input_str[int(n / 2): n]
    temp_str = list(right + left)

    for i in range(0, int(len(temp_str)/2)):
        if right[len(right) - i - 1] == left[i]:
            del temp_str[n - i - 1]
            del temp_str[i]
        # print("+++++++++++++\n")
    print(temp_str)
    print(len(temp_str))


string_minimization("aabcccabba")
