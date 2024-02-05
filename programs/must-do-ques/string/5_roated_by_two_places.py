def is_rotated(str1, str2, k=2):
    if len(str1) != len(str2):
        return False

    n = len(str1)
    clock_rot = ""  # Elements are shifted in right
    antiknock_rot = ""  # Elements are shifted in left
    antiknock_rot = antiknock_rot + str2[n - k:] + str2[0: n - k]
    clock_rot = clock_rot + str2[k:] + str2[0: k]
    return str1 == clock_rot or str1 == antiknock_rot


str1 = "amazon"
str2 = "azonam"
if is_rotated(str1, str2):
    print("Yes")
else:
    print("No")
