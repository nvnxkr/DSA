'''
Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.

 

Example 1:

Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we do not need any insertions.
Example 2:

Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".
Example 3:

Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel".
 

'''

class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp=[[-1]*n for _ in range(n)]

        def solve(i, j):
            if i >= j:
                dp[i][j]= 0
                return dp[i][j]
            
            if dp[i][j]!=-1:
                return dp[i][j]

            if s[i] == s[j]:
                dp[i][j]=solve(i + 1, j - 1)
                return dp[i][j]

            else:
                dp[i][j]=1 + min(solve(i, j - 1), solve(i + 1, j))
                return dp[i][j]

        return solve(0, n - 1)
    

class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[10**5] * (n + 1) for _ in range(n + 1)]

        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = length + i - 1

                if length == 1:
                    dp[i][j] = 0

                elif length == 2:
                    dp[i][j] = 1 if s[i] != s[j] else 0
                else:
                    if s[i] == s[j]:
                        dp[i][j] = dp[i + 1][j - 1]
                    else:
                        dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]
