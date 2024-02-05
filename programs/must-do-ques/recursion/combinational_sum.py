"""
Given an array of positive integers arr[] and a sum x, find all unique combinations in arr[] where the sum is equal to x.
The same repeated number may be chosen from arr[] unlimited number of times. Elements in a combination (a1, a2, …, ak)
must be printed in non-descending order. (ie, a1 <= a2 <= … <= ak).

The combinations themselves must be sorted in ascending order, i.e., the combination with smallest first element should
be printed first. If there is no combination possible the print "Empty" (without quotes).

Examples:

Input : arr[] = 2, 4, 6, 8
            x = 8
Output : [2, 2, 2, 2]
         [2, 2, 4]
         [2, 6]
         [4, 4]
         [8]

Algorithms:

1. Sort the array(non-decreasing).
2. First remove all the duplicates from array.
3. Then use recursion and backtracking to solve
   the problem.
   (A) If at any time sub-problem sum == 0 then
       add that array to the result (vector of
       vectors).
   (B) Else if sum if negative then ignore that
       sub-problem.
   (C) Else insert the present array in that
       index to the current vector and call
       the function with sum = sum-ar[index] and
       index = index, then pop that element from
       current index (backtrack) and call the
       function with sum = sum and index = index+1
"""
