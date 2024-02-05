"""
Let n be the size of the list of strings and l be the average length of a string in the list of strings.

Time complexity:
----------------
The time complexity will be O(n×l) because, for each string, we’ll traverse through each of its characters to generate
the key.

Space complexity:
-----------------
In the worst case, we will have a key for each individual string, so the space complexity will be O(n).
"""


def combine_messages(messages):
    # Function to generate keys
    def generate_key(message):
        key = ""
        for i in range(1, len(message)):
            # Compute difference of adjacent characters
            diff = (ord(message[i]) - ord(message[i - 1]))

            # Handle the wrap around case
            if (diff < 0):
                diff += 26
            # Construct the key string
            key += str(diff) + ", "

        return key

    message_group = {}
    for i in range(len(messages)):
        # Get key for current message
        message_key = generate_key(messages[i])

        # Add key and assign message to it
        if message_key not in message_group:
            message_group[message_key] = [messages[i]]
        # Assign message to existing key
        else:
            message_group[message_key].append(messages[i])

    return message_group


# Driver code
messages = ["lmn", "mno", "azb", "bac", "yza", "bdfg"]
groups = combine_messages(messages)
print("The Grouped Messages are:\n")
for group in groups:
    print(groups[group])
