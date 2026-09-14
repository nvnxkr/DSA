"""
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.



Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation:
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix =
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation:
There are 6 squares of side 1.
There is 1 square of side 2.
Total number of squares = 6 + 1 = 7.
"""


from typing import List


class Solution:
    def countSquares(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        dp = [[0] * (n) for _ in range(m)]
        for i in range(m):
            dp[i][0] = mat[i][0]
        for i in range(n):
            dp[0][i] = mat[0][i]

        for i in range(1, m):
            for j in range(1, n):
                if mat[i][j] == 1:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                else:
                    dp[i][j] = 0
        total = 0
        print(dp)
        for i in range(m):
            for j in range(n):
                total += dp[i][j]
        return total

sol = Solution()
print(sol.countSquares([[0,1,1,1],[1,1,1,1],[0,1,1,1]]))
print(sol.countSquares([[1,0,1],[1,1,0],[1,1,0]]))