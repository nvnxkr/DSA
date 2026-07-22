'''
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
'''

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = [[-1] * (m + 1) for _ in range(n + 1)]

        def solve(i, j):
            n = len(word1)
            m = len(word2)

            if j == m:
                return n - i
            if i == n:
                return m - j

            if dp[i][j] != -1:
                return dp[i][j]

            if word1[i] == word2[j]:
                dp[i][j] = solve(i + 1, j + 1)  # nothing to do so i+1 and j+1
                return dp[i][j]

            dp[i][j] = 1 + min(
                solve(i, j + 1),  # insertion
                solve(i + 1, j),  # Deletion
                solve(i + 1, j + 1),  # Replace
            )

            return dp[i][j]

        return solve(0, 0)
