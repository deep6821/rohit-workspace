s = "i like this input string"
words = s.split(" ")
result = []
for word in words:
    result.insert(0, word)

print(" ".join(result))
