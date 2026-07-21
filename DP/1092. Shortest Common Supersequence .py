'''
Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.

 

Example 1:

Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.
Example 2:

Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
Output: "aaaaaaaa"
 
'''

# another approach is to find the longest common subsequence of the two strings and then build the shortest common supersequence from it. The length of the shortest common supersequence can be calculated as:
# length of shortest common supersequence = length of str1 + length of str2 - length of longest common subsequence

class Solution:
    def shortestCommonSupersequence(self, s1: str, s2: str) -> str:
        dp = [[-1] * 1001 for _ in range(1001)]
        n = len(s1)
        m = len(s2)

        # def solve(i,j,s1,s2):

        #     if i==len(s1):
        #         return len(s2)-j
        #     if j==len(s2):
        #         return len(s1)-i
        #     if dp[i][j]!=-1:
        #         return dp[i][j]
        #     if s1[i]==s2[j]:
        #         dp[i][j]=1+solve(i+1,j+1,s1,s2)
        #         return dp[i][j]
        #     else:
        #         dp[i][j]=min(1+solve(i+1,j,s1,s2),1+solve(i,j+1,s1,s2))
        #         return dp[i][j]

        # solve(0,0,s1,s2)

        for i in range(n + 1):
            dp[i][m] = n - i
        for j in range(m + 1):
            dp[n][j] = m - j

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):

                if s1[i] == s2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = min(1 + dp[i + 1][j], 1 + dp[i][j + 1])

        # return dp[0][0]

        """
        Dp will look like this 

                     c  a  b end
                a    5  4  4  4
                b    5  4  3  3
                a    4  3  3  2
                c    3  3  2  1
                end  3  2  1  0 --> end value comes from 'for loop' (( edge case ))
                              
        """

        # find the Shortest Common Supersequence from dp table
        i, j = 0, 0
        res = []
        while i < n and j < m:
            if s1[i] == s2[j]:
                res.append(s1[i])
                i += 1
                j += 1
            elif dp[i + 1][j] < dp[i][j + 1]:
                res.append(s1[i])
                i += 1
            else:
                res.append(s2[j])
                j += 1

        while i < n:
            res.append(s1[i])
            i += 1

        while j < m:
            res.append(s2[j])
            j += 1

        return "".join(res)

sol = Solution()
print(sol.shortestCommonSupersequence("abac", "cab"))