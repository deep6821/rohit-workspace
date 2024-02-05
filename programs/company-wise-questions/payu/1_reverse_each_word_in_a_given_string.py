def reverse_each_words(string):
    result = []
    words = string.split(" ")
    for word in words:
        result.append(word[::-1])

    output_str = " ".join(result)
    print(output_str)


string = "Rohit Kumar Pandey"
reverse_each_words(string)
