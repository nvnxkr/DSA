'''
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
Example 2:


Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
 
'''

from typing import List

class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[-1] * (n + 1) for _ in range(m + 1)]

        def solve(i, j):
            if i >= m or j >= n:
                dp[i][j] = 0
                return dp[i][j]
            if grid[i][j] == 1:
                dp[i][j] = 0
                return dp[i][j]
            if dp[i][j] != -1:
                return dp[i][j]
            if i == m - 1 and j == n - 1:
                dp[i][j] = 1
                return dp[i][j]

            dp[i][j] = solve(i + 1, j) + solve(i, j + 1)
            return dp[i][j]

        return solve(0, 0)


class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        n=len(grid[0])
        m=len(grid)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        if grid[0][0] == 1:
            return 0

        dp[0][0]=1

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    dp[i][j]=0
                elif i==0 and j==0:
                    continue

                else:
                    up=dp[i-1][j] if i>0 else 0
                    left=dp[i][j-1] if j>0 else 0
                    dp[i][j]=up+left
        
        return dp[m-1][n-1]

sol = Solution()
print(sol.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))