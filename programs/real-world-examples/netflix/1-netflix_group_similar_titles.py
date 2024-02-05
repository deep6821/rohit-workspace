"""
Let n be the size of the list of strings, and k be the maximum length that a single string can have.

Complexity measures:
-------------------
Let n be the size of the list of strings, and k be the maximum length that a single string can have.

Time Complexity: We are counting each letter for each string in a list, so the time complexity will be O(n×k).
Space complexity: Since every string is being stored as a value in the dictionary whose size can be n, and the size of
the string can be k, so space complexity is O(n×k).


"""


def group_titles(strs):
    res = {}
    for s in strs:
        count = [0] * 26
        for c in s:
            index = ord(c) - ord('a')
            count[index] += 1
        key = tuple(count)
        if key in res:
            res[key].append(s)
        else:
            res[key] = [s]
    return res.values()


# Driver code
titles = ["duel", "dule", "speed", "spede", "deul", "cars"]
gt = list(group_titles(titles))
print("GT: ", gt)
query = "spede"

# Searching for all titles
for g in gt:
    if query in g:
        print(g)
