'''
You are given an integer array nums and two integers lower and upper.

A missing integer is an integer in the inclusive range [lower, upper] that does not appear in nums.

Return a 2D integer array where each element is of the form [start, end], representing a contiguous range of missing integers. Return the ranges in increasing order. If there are no missing integers, return an empty array.

Note: Consecutive missing integers should be grouped into a single range.

 

Example 1:

Input: nums = [3,9,7], lower = 1, upper = 12

Output: [[1,2],[4,6],[8,8],[10,12]]

Explanation:

The missing integers are [1, 2, 4, 5, 6, 8, 10, 11, 12].
Grouping the missing integers into the minimum number of contiguous ranges, we get [1, 2], [4, 6], [8, 8], and [10, 12].
Therefore, the answer is [[1, 2], [4, 6], [8, 8], [10, 12]].
Example 2:

Input: nums = [1,1], lower = 5, upper = 7

Output: [[5,7]]

Explanation:

The missing integers are [5, 6, 7].
Grouping the missing integers into the minimum number of contiguous ranges, we get [5, 7].
Therefore, the answer is [[5, 7]].
'''

class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:

        n = upper - lower + 1
        arr = [False] * n

        for x in nums:
            if lower <= x <= upper:
                arr[x - lower] = True
        l = 0
        r = 0
        ans = []
        while r < n:
            if arr[r]:
                l += 1
                r += 1
                continue
            while r < n and not arr[r]:
                r += 1
            ans.append([lower + l, lower + r - 1])
            l = r
        return ans
