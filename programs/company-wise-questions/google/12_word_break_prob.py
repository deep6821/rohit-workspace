# Time complexity : O(2^n)
# Space complexity : O(n): The depth of the recursion tree can go upto n.


def word_break_problem_using_recursion(word, word_list, out=""):
    if len(word) == 0:
        print("out: ", out)
        return
    for i in range(1, len(word) + 1):
        prefix = word[:i]
        suffix = word[i:]
        if prefix in word_list:
            word_break_problem_using_recursion(
                suffix,
                word_list,
                out + " " + prefix
            )


def word_break_problem_using_dp(word, word_list):
    result = []
    max_l = len(max(word_list, key=len))
    length = len(word) + 1
    for j in range(1, length):
        i = j - 1
        flag = 0
        ans = []
        x = 0
        # Letting setting x to j - max_l optimization,
        # the code will work even if x is always set to 0
        if j > max_l:
            x = j - max_l
        while i >= x:
            if word[i:j] in word_list:
                if i > 0 and result[(i - 1)]:
                    # appending the word to all the valid sentences
                    # formed by the substring ending at i-1
                    temp = list((map(lambda y: y + " " + word[i:j], result[(i - 1)])))
                    for elem in temp:
                        ans.append(elem)
                    flag = 2
                else:
                    flag = 1
                    result.append([word[i:j]])
            i = i - 1

        # if the substring does not belong to the
        # dictionary append an empty list to result
        if flag == 0:
            result.append([])
        if flag == 2:
            result.append(ans)
    if word in word_list:
        result[len(word) - 1].append(word)

    # temp = ", result [{}]: "
    # for i in range(len(word)):
    #     print("s:", word[:(i + 1)], temp.format(i), result[i])

    # If result[len(s)-1] is empty then the string cannot be
    # broken down into valid strings
    print("Final answer for cookies and cream:", result[len(word) - 1])


def word_break(word, word_list):
    word_set = set(word_list)  # can reduce the search complexity to O(1)
    dp = [False for i in range(len(word) + 1)]
    dp[0] = True
    for i in range(1, len(word) + 1):
        for j in range(i):
            if dp[j] and word[j:i] in word_set:
                dp[i] = True
                break
    return dp[-1]


# ---------------------------------------------------------------------
word = "cookiesandcream"
word_list = ["cookie", "cookies", "and", "sand", "cream"]
# word = "Iamnun"
# word_list = ["I", "am", "nun"]

# print(word_break_problem_using_recursion(word, word_list))
# word_break_problem_using_dp(word, word_list)
# print(word_break_problem_using_dp2(word, word_list))
print(word_break_problem_using_recursion(word, word_list))
