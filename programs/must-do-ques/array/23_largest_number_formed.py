from itertools import permutations


def largest_number(arr):
    lst = []
    for i in permutations(arr, len(arr)):
        lst.append("".join(map(str, i)))

    print(max(lst))


largest_number([54, 546, 548, 60])
