'''
You are given a 0-indexed m x n matrix grid consisting of positive integers.

You can start at any cell in the first column of the matrix, and traverse the grid in the following way:

From a cell (row, col), you can move to any of the cells: (row - 1, col + 1), (row, col + 1) and (row + 1, col + 1) such that the value of the cell you move to, should be strictly bigger than the value of the current cell.
Return the maximum number of moves that you can perform.

 

Example 1:


Input: grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
Output: 3
Explanation: We can start at the cell (0, 0) and make the following moves:
- (0, 0) -> (0, 1).
- (0, 1) -> (1, 2).
- (1, 2) -> (2, 3).
It can be shown that it is the maximum number of moves that can be made.
Example 2:


Input: grid = [[3,2,4],[2,1,9],[1,1,7]]
Output: 0
Explanation: Starting from any cell in the first column we cannot perform any moves.
'''

from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[-1] * (n+1) for _ in range(m+1)]

        def solve(i, j):
            if i == m or j == n - 1:
                dp[i][j] = 0
                return dp[i][j]

            if dp[i][j] != -1:
                return dp[i][j]

            up = 0
            same = 0
            down = 0
            if i > 0 and grid[i - 1][j + 1] > grid[i][j]:
                up = 1 + solve(i - 1, j + 1)
            if grid[i][j + 1] > grid[i][j]:
                same = 1 + solve(i, j + 1)
            if i < m - 1 and grid[i + 1][j + 1] > grid[i][j]:
                down = 1 + solve(i + 1, j + 1)

            dp[i][j] = max(up, same, down)
            return dp[i][j]

        ans = 0

        for i in range(m):
            ans = max(ans, solve(i, 0))

        return ans

sol = Solution()
print(sol.maxMoves([[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]))