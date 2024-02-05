# Time Complexity: O(M*N) where M and N are sizes of given arrays.
def number_of_pairs(arr1, arr2):
    ans = 0
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if pow(arr1[i], arr2[j]) > pow(arr2[j], arr1[i]):
                ans += 1
                print(arr1[i], arr2[j])
    print(ans)


arr1 = [2, 1, 6]
arr2 = [1, 5]
number_of_pairs(arr1, arr2)
