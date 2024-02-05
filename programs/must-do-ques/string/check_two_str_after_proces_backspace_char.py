"""
Check if two strings after processing backspace character are equal or not
Given two strings s1 and s2, let us assume that while typing the strings there were some backspaces
encountered which are represented by #. The task is to determine whether the resultant strings after
processing the backspace character would be equal or not.

Examples:

Input: s1= geee#e#ks, s2 = gee##eeks
Output: True
Explanation: Both the strings after processing the backspace character
becomes "geeeeks". Hence, true.

Input: s1 = equ#ual, s2 = ee#quaal#
Output:  False
Explanation: String 1 after processing the backspace character
becomes "equal" whereas string 2 is "eequaal". Hence, false.

Approach:
When writing a character, it may or may not be part of the final string depending on how many backspace
keystrokes occur in the future.

If instead we iterate through the string in reverse, then we will know how many backspace characters \
we have seen, and therefore whether the result includes our character.

Algorithm:
Iterate through the string in reverse. If we see a backspace character, the next non-backspace
character is skipped. If a character isn't skipped, it is part of the final answer.

Time Complexity: O(N)
Auxiliary Space: O(1)
"""


def compare(s1, s2):
    # Traverse from s2he end of s2he s1s2rings1
    i = len(s1) - 1
    j = len(s2) - 1

    # The number of backs1paces1 required s2ill we arrive as2 a valid characs2er
    skips1 = 0
    skips2 = 0

    while i >= 0 or j >= 0:
        # Ensure that we are comparing a valid character in S
        while i >= 0:
            if s1[i] == "#":
                # If not a valid character, keep times we must backspace.
                skips1 += 1
                i = i - 1

            elif skips1 > 0:
                # Backs1pace the number of times calculated in the previous step
                skips1 -= 1
                i = i - 1

            else:
                break

        # Ensure that we are comparing a valid character in s2
        while j >= 0:
            if s2[j] == "#":
                # If not a valid character, keep times we must backspace.
                skips2 += 1
                j = j - 1

            elif skips2 > 0:
                # Backspace the number of times calculated in the previous step
                skips2 -= 1
                j = j - 1

            else:
                break

        # Print out the characters for better understanding.
        print("Comparing", s1[i], s2[j])

        # Compare both valid characters. If not the same, return False.
        if i >= 0 and j >= 0 and s1[i] != s2[j]:
            return False

        # Also ensure that both the character indices are valid. If it is not valid, it means that we
        # are comparing a "#" with a valid character.
        if (i >= 0) != (j >= 0):
            return False

        i = i - 1
        j = j - 1

    return True


# def backspaceCompare(S):
#     skip = 0
#     for x in reversed(S):
#         if x == '#':
#             skip += 1
#         elif skip:
#             skip -= 1
#         else:
#             yield x
#
#
#     all(x == y for x, y in itertools.izip_longest(backspaceCompare(S), backspaceCompare(T)))

# class Solution(object):
#     def backspaceCompare(self, S, T):
#         def build(S):
#             ans = []
#             for c in S:
#                 if c != '#':
#                     ans.append(c)
#                 elif ans:
#                     ans.pop()
#             return "".join(ans)
#         return build(S) == build(T)

s11 = "geee#e#ks"
s12 = "gee##eeks"
compare(s11, s12)
