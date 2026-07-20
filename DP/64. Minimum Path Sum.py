'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

 

Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 200
'''

from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        mini = 10**8
        total = grid[0][0]
        dp = [[-1] * (n + 1) for _ in range(m + 1)]

        def solve(i, j):
            if i >= m or j >= n:
                dp[i][j] = float("inf")
                return dp[i][j]

            if i == m - 1 and j == n - 1:
                dp[i][j] = grid[i][j]
                return dp[i][j]

            if dp[i][j] != -1:
                return dp[i][j]

            right = solve(i + 1, j)
            down = solve(i, j + 1)

            dp[i][j] = grid[i][j] + min(right, down)
            return dp[i][j]

        return solve(0, 0)

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp = [[0] * (n ) for _ in range(m)]
        total=0
        # fill first row and first column
        for i in range(m):
            total+=grid[i][0]
            dp[i][0]=total

        total=0
        for i in range(n):
            total+=grid[0][i]
            dp[0][i]=total

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=grid[i][j]+min(dp[i-1][j],dp[i][j-1])

        return dp[m-1][n-1]