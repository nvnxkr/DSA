'''
You are given three integers n, m and k. Consider the following algorithm to find the maximum element of an array of positive integers:


You should build the array arr which has the following properties:

arr has exactly n integers.
1 <= arr[i] <= m where (0 <= i < n).
After applying the mentioned algorithm to arr, the value search_cost is equal to k.
Return the number of ways to build the array arr under the mentioned conditions. As the answer may grow large, the answer must be computed modulo 109 + 7.

 

Example 1:

Input: n = 2, m = 3, k = 1
Output: 6
Explanation: The possible arrays are [1, 1], [2, 1], [2, 2], [3, 1], [3, 2] [3, 3]
Example 2:

Input: n = 5, m = 2, k = 3
Output: 0
Explanation: There are no possible arrays that satisfy the mentioned conditions.
Example 3:

Input: n = 9, m = 1, k = 1
Output: 1
Explanation: The only possible array is [1, 1, 1, 1, 1, 1, 1, 1, 1]
 
'''

class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        sc = 0
        maxi = -1
        MOD = 10**9 + 7

        dp = [[[-1 for _ in range(51)] for _ in range(101)] for _ in range(51)]

        def solve(i, sc, maxi):
            if i == n:
                if sc == k:
                    return 1
                if sc > k:
                    return 0
                return 0

            if dp[i][maxi][sc] != -1:
                return dp[i][maxi][sc]

            result = 0

            for j in range(1, m + 1):
                if j > maxi:
                    result += solve(i + 1, sc + 1, j)
                else:
                    result += solve(i + 1, sc, maxi)
            dp[i][maxi][sc] = result % MOD

            return dp[i][maxi][sc]

        return solve(0, 0, -1)

sol = Solution()
print(sol.numOfArrays(2, 3, 1))
