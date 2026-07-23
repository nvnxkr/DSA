'''
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 
'''
# Top down approach

class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        dp = [[0] * n for _ in range(n)]
        maxLen = 0  # length of the longest palindrome
        start = -1  # starting index of the longest palindrome

        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if length == 1:
                    dp[i][j] = 1
                elif length == 2:
                    dp[i][j] = 1 if s[i] == s[j] else 0
                else:
                    dp[i][j] = 1 if (s[i] == s[j] and dp[i + 1][j - 1] == 1) else 0

                if dp[i][j] and j - i + 1 > maxLen:
                    maxLen = j - i + 1
                    start = i

        ans = s[start : maxLen + start]
        return ans

sol = Solution()
print(sol.longestPalindrome("babad"))
