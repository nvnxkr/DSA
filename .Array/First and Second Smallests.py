'''
Given an array, arr[] of integers, your task is to return the smallest and second smallest element in the array. If the smallest and second smallest do not exist, return -1.

Examples:

Input: arr[] = [2, 4, 3, 5, 6]
Output: [2, 3] 
Explanation: 2 and 3 are respectively the smallest and second smallest elements in the array.
Input: arr[] = [1, 1, 1]
Output: [-1]
Explanation: Only element is 1 which is smallest, so there is no second smallest element.
Constraints:
1 ≤ arr.size ≤105
1 ≤ arr[i] ≤ 105
'''

class Solution:
    def minAnd2ndMin(self, arr):
        # code here
        fir = 10 ** 8
        sec = 10 ** 8

        for num in arr:
            if num<fir:
                sec = fir
                fir = num
            if num>fir and num<sec:
                sec = num

        if sec == 10 ** 8:
            return [-1]

        return [fir, sec]

sol = Solution()
arr = [2, 4, 3, 5, 6]
print(sol.minAnd2ndMin(arr))  # Output: [2, 3]