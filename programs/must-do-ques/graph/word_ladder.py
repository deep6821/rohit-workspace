"""
Word Ladder (Length of shortest chain to reach a target word)
-------------------------------------------------------------

Given a dictionary, and two words ‘start’ and ‘target’ (both of same length). Find length of the smallest chain from
‘start’ to ‘target’ if it exists, such that adjacent words in the chain only differ by one character and each word in
the chain is a valid word i.e., it exists in the dictionary.
It may be assumed that the ‘target’ word exists in dictionary and length of all dictionary words is same.

Example:
Input:  Dictionary = {POON, PLEE, SAME, POIE, PLEA, PLIE, POIN}
             start = TOON
             target = PLEA
Output: 7
Explanation: TOON - POON - POIN - POIE - PLIE - PLEE - PLEA
"""

from collections import deque


def is_adjacent(a, b):
    count = 0
    for i in range(0, len(a)):
        if a[i] != b[i]:
            count += 1
    if count == 1:
        # return count
        return True

    return False


def shortest_chain_length(start, target, word_list):
    if start == target:
        return 1

    queue = deque()
    queue.append(start)
    count = {start: 1}
    word_list.append(target)
    while True:
        try:
            element = queue.popleft()
        except IndexError:
            break

        for word in word_list:
            if is_adjacent(element, word) == 1:
                if word == target:
                    print(word, ">>>>>", target)
                    return count[element] + 1

                count[word] = count[element] + 1
                queue.append(word)
    return 0


# word_list = ["POON", "PLEE", "SAME", "POIE", "PLEA", "PLIE", "POIN"]
# start = "TOON"
# target = "PLEA"
word_list = ["hot", "dot", "dog", "lot", "log"]
start = "hit"
target = "cog"
print(shortest_chain_length(start, target, word_list))
