def str_to_int(words):
    result = []
    for word in words:
        if not word.isalnum():
            return False
        else:
            result.append(word)

    return "".join(result)


s = "234234 5 asdasd 34"
words = s.split(" ")
result = str_to_int(words)
print(result)

