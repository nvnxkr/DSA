'''
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
Example 2:


Input: matrix = [["0","1"],["1","0"]]
Output: 1
Example 3:

Input: matrix = [["0"]]
Output: 0
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.
'''

from copy import deepcopy
from typing import List


class Solution:
    def maximalSquare(self, mat: List[List[str]]) -> int:
        m = len(mat)
        n = len(mat[0])
        dp = [mat[i][:] for i in range(m)]
        maxi = 0

        for i in range(m):
            for j in range(n):
                if mat[i][j] == "1":
                    if i > 0 and j > 0:
                        dp[i][j] = 1 + min(
                            int(dp[i - 1][j]), int(dp[i][j - 1]), int(dp[i - 1][j - 1])
                        )
                else:
                    dp[i][j] = 0

                maxi = max(maxi, int(dp[i][j]))

        return maxi**2

sol = Solution()
print(sol.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
print(sol.maximalSquare([["0","1"],["1","0"]]))