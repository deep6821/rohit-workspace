# The idea is simple, we consider each prefix and search it in dictionary.
# If the prefix is present in dictionary, we recur for rest of the string
# (or suffix).
def word_break(word_list, word):
    if word == '':
        return True
    else:
        word_len = len(word)
        return any(
            [(word[:i] in word_list) and word_break(word_list, word[i:]) for i
             in range(1, word_len + 1)])


word_list = ["i", "like", "sam", "sung", "samsung", "mobile", "ice",
             "cream", "icecream", "man", "go", "mango"]
word = "ilikesamsung"
print(word_break(word_list, word))
