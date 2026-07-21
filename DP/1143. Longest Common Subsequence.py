'''
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        dp=[[-1]*1001 for _ in range(1001)]
        
        def solve(i,j,text1,text2):
            n=len(text1)
            m=len(text2)

            if i==n or j==m:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            
            if text1[i]==text2[j]:
                dp[i][j]=1+solve(i+1,j+1,text1,text2)
                return dp[i][j]
            
            else:
                take_1=solve(i,j+1,text1,text2)
                take_2=solve(i+1,j,text1,text2)
                dp[i][j]=max(take_1,take_2)
                return dp[i][j]
        
        return solve(0,0,text1,text2)
        


class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:

        n = len(s1)
        m = len(s2)
        dp = [[-1] * 1001 for _ in range(1001)]

        for j in range(m + 1):
            dp[n][j] = 0

        for i in range(n + 1):
            dp[i][m] = 0

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]

                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]

sol = Solution()
text1 = "abcde"
text2 = "ace"
print(sol.longestCommonSubsequence(text1, text2))
