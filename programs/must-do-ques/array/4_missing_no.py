# TC: 0(n) and SC: 0(1)
def get_missing_num1(arr):
    n = len(arr)
    total = 1
    for i in range(2, n + 2):
        total += i
        total -= arr[i - 2]
    return total


# TC: 0(n) and SC: 0(1)
def get_missing_num2(arr):
    n = len(arr)
    x1 = arr[0]
    x2 = 1
    for i in range(1, n):
        x1 = x1 ^ arr[i]

    for i in range(2, n + 2):
        x2 = x2 ^ i

    return x1 ^ x2


arr = [1, 2, 4, 5, 6]
missing_no = get_missing_num1(arr)
print(missing_no)
missing_no2 = get_missing_num2(arr)
print(missing_no2)
