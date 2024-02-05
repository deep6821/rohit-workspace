"""
Let sl be the length of S and wl be the length of W.

Time complexity:
----------------
We’ll be traversing both the strings, but the string with greater length will dominate the time complexity.
Therefore, we can consider O(max(sl, wl)) to be considered the worst-case time complexity.

Space complexity:
-----------------
The space complexity will be O(1) because we are only manipulating two pointers.
"""


def flag_words(S, W):
    def repeated_letters(s, ind):
        temp = ind
        while temp < len(s) and s[temp] == s[ind]:
            temp += 1
        return temp - ind

    if not S and not W:
        return False

    i, j = 0, 0
    while i < len(S) and j < len(W):
        if S[i] == W[j]:
            len1 = repeated_letters(S, i)
            len2 = repeated_letters(W, j)
            if (len1 < 3 and len1 != len2) or (len1 >= 3 and len1 < len2):
                return False

            i += len1
            j += len2
        else:
            return False

    return (i == len(S)) and (j == len(W))


# Driver code

S = "mooooronnn"  # modified word
W = "moron"  # original word

if flag_words(S, W):
    print("Word Flagged")
    print("The word", '"' + S + '"', "is a possible morph of", '"' + W + '"')
else:
    print("Word Safe")