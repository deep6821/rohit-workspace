"""
sort () and sorted(): It’s called Timsort. It's an exceptionally adaptive merge sort, which is
miraculous in practice, but asymptotically it’s no better than merge sort

Time complexity of sort and sorted : O(n log n) both on average and in the worst case. sorted is like
sort except that the first builds a new sorted list from an iterable while sort do sort in place.

Space complexity of sort and sorted: sort() worst case space complexity is O(N) and best case O(1) and
sorted()

timsort can require a temp array containing as many as N//2 pointers, which means as many as 2*N extra
bytes on 32-bit boxes. It can be expected to require a temp array this large when sorting random data;
on data with significant structure, it may get away without using any extra heap memory.
"""


def using_bubble_sort(sub_li):
    l = len(sub_li)
    for i in range(0, l):
        for j in range(0, l - i - 1):
            if sub_li[j][1] > sub_li[j + 1][1]:
                tempo = sub_li[j]
                sub_li[j] = sub_li[j + 1]
                sub_li[j + 1] = tempo
    return sub_li


def using_sort_method(sub_li):
    sub_li.sort(key=lambda x: x[1])
    return sub_li


def using_sorted_method(sub_li):
    return sorted(sub_li, key=lambda x: x[1])


sub_li = [['rishav', 10], ['akash', 5], ['ram', 20], ['gaurav', 15]]
print(using_bubble_sort(sub_li))
