"""
Maximum Mismatches:
-------------------
You are given a string S of length N, you can select and reverse any substring of S of any length.
You are allowed to perform this operation many numbers of times.

Your task is to determine the maximum number of mismatches by performing the operations.

Mismatch(S): is defined the number of corresponding positions where characters are different in S
Reverse(S): for example, the string abca has 2 mismatches whereas aaaa has none

Input Format:
. First line: T(number of test cases)
. For each test case:
   . First line: N(length of the string)
   . Next line: String S of length N

Output Format:
For each test case, print the number of maximum mismatches in a new line

Sample Input:           Sample Output:
3                       4
4                       6
abab                    0
9
aatacanaa
5
bbbbb
"""

t = int(input())
for i in range(0, t):
    n = int(input())
    s = input()
    str1 = s[0: int(n / 2)]
    str2 = s[int(n / 2): n]
    result = str2 + str1

    count = 1
    for i in range(0, n - 1):
        if result[i] != result[i + 1]:
            count += 1

    if count == 1:
        print(count - 1)
    else:
        print(count)
