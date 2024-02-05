# Printing frequency of each character just after its consecutive occurrences
# Input : GeeeEEKKKss
# Output : G1e3E2K3s2


def count_consecutive_occurrences1(s):
    count = 1
    freq = {}
    for i in range(0, len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
            freq[s[i]] = count
        else:
            count = 1
    print(freq)


def count_consecutive_occurrences2(s):
    count = 1
    freq = {}
    for i in range(0, len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
            freq[s[i]] = count
        else:
            freq[s[i]] = count
            count = 1
    print(freq)


def count_frequency_of_word1(words):
    count = {}
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    print(count)


def count_frequency_of_word2(words):
    from collections import Counter
    counts = Counter(words)
    print(counts)


def check_if_one_tuple_is_subset_of_other(tuple1, tuple2):
    res1 = set(test_tup2).issubset(test_tup1)
    print(res1)
    res2 = all(ele in test_tup1 for ele in test_tup2)
    print(res2)

"""
Difference between Multiprocessing and Multithreading.
-----------------------------------------------------
Both Multiprocessing and Multithreading are used to increase the computing power of a system.

Multiprocessing:
++++++++++++++++
Multiprocessing is a system that has more than one or two processors. In Multiprocessing, CPUs are added for increasing 
computing speed of the system. Because of Multiprocessing, There are many processes are executed simultaneously.
Multiprocessing are classified into two categories:

1. Symmetric Multiprocessing
2. Asymmetric Multiprocessing

Multithreading:
+++++++++++++++
Multithreading is a system in which multiple threads are created of a process for increasing the computing speed of the 
system. In 3-concurrencey, many threads of a process are executed simultaneously and process creation in 3-concurrencey 
is done according to economical.

Difference between Multiprocessing and Multithreading:
++++++++++++++++++++++++++++++++++++++++++++++++++++++

S.NO 	Multiprocessing 	                            Multithreading
1. 	    In Multiprocessing, CPUs are added for          In Multithreading, many threads are created of a single process
        increasing computing power.                     for increasing computing power.

2. 	    In Multiprocessing, Many processes are          While in 3-concurrencey, many threads of a process a
        executed simultaneously. 	                    process are executed simultaneously.

3. 	    Multiprocessing are classified into             While Multithreading is not classified in any categories
        Symmetric and Asymmetric.

4. 	    In Multiprocessing, Process creation is a       While in Multithreading, process creation is according to
        time-consuming process.                         economical.

"""

"""
- Serialization VS De-serialization
- Request Related question
"""



word1 = "100011010"
word2 = "GeeeEEKKKss"
count_consecutive_occurrences1(word1)
count_consecutive_occurrences2(word2)
count_frequency_of_word1(word1)
count_frequency_of_word2(word1)
test_tup1 = (10, 4, 5, 6)
test_tup2 = (5, 10)
check_if_one_tuple_is_subset_of_other(test_tup1, test_tup2)