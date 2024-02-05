"""
How to print maximum number of A’s using given four keys

Below is the problem statement.
Imagine you have a special keyboard with the following keys:
Key 1:  Prints 'A' on screen
Key 2: (Ctrl-A): Select screen
Key 3: (Ctrl-C): Copy selection to buffer
Key 4: (Ctrl-V): Print buffer on screen appending it after what has already been printed.

If you can only press the keyboard for N times (with the above four keys), write a program to produce maximum numbers
of A's. That is to say, the input parameter is N (No. of keys that you can press), the  output is
M (No. of As that you can produce).
"""


def find_optimal1(num):
    if num <= 6:
        return num

    count = 0
    for i in range(num-3, 0, -1):
        curr = (num-i-1) * find_optimal1(i)
        if curr > count:
            count = curr
    return count


def find_optimal2(num):
    if num <= 6:
        return num

    screen = [0] * num
    for i in range(1, 7):
        screen[i-1] = i

    for i in range(7, num+1):
        screen[i-1] = 0
        for j in range(i-3, 0, -1):
            curr = (i-j-1)* screen[j-1]
            if curr > screen[i-1]:
                screen[i-1] = curr

    return screen[num-1]


def find_optimal3(num):
    if num <= 6:
        return num

    screen = [0] * num
    for i in range(1, 7):
        screen[i-1] = i

    for i in range(7, num+1):
        # for any keystroke n, we will need to choose between:-
        # 1. pressing Ctrl-V once after copying the
        # A's obtained by n-3 keystrokes.

        # 2. pressing Ctrl-V twice after copying the A's
        # obtained by n-4 keystrokes.

        # 3. pressing Ctrl-V thrice after copying the A's
        # obtained by n-5 keystrokes.
        screen[i - 1] = max(2 * screen[i - 4], max(3 * screen[i - 5], 4 * screen[i - 6]))

    return screen[num-1]


for num in range(1, 10):
    print("Maximum number of As with ", num, "keystrokes is: ", find_optimal1(num))
