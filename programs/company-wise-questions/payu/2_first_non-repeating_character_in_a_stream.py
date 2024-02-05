MAX_CHAR = 256


def find_first_non_repeating_char():
    dll_array = [] * MAX_CHAR
    repeated_array = [False] * MAX_CHAR
    stream = "geekforgeekandgeeksandquizfor"
    for i in range(len(stream)):
        x = stream[i]
        print("Reading " + x + " from stream")
        if not repeated_array[ord(x)]:
            if not x in dll_array:
                dll_array.append(x)
            else:
                dll_array.remove(x)
                repeated_array[ord(x)] = True

        if len(dll_array) != 0:
            print("First non-repeating character so far is ")
            print(str(dll_array[0]))


find_first_non_repeating_char()
