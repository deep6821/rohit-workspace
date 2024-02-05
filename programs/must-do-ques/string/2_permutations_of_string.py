# Time Complexity: O(n*n!) Note that there are n! permutations and it requires O(n) time to print a a permutation.
def permutate(s, l, r):
    if l == r:
        print("".join(s))

    for i in range(l, r):
        s[l], s[i] = s[i], s[l]
        permutate(s, l + 1, r)
        s[l], s[i] = s[i], s[l]


s = "ABC"
l = 0
r = len(s)
permutate(list(s), l, r)
