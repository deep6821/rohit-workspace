def value(s):
    if s == "I":
        return 1
    elif s == "V":
        return 5
    elif s == "X":
        return 10
    elif s == "L":
        return 50
    elif s == "C":
        return 100
    elif s == "D":
        return 500
    elif s == "M":
        return 1000
    else:
        return -1


def roman_to_int(s):
    i = 0
    res = 0
    while i <= len(s)-1:
        s1 = value(s[i])
        if 1+1 < len(s):
            s2 = value(s[i+1])

            if s1 >= s2:
                res = res + s1
                i = i + 1
            else:
                res = res + s2-s1
                i = i + 2
        else:
            res = res + s1
            i = i + 1
    return res


print(roman_to_int("MCMIV"))