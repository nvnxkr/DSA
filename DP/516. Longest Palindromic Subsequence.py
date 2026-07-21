'''
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
'''

from functools import lru_cache


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n=len(s)

        @lru_cache(None)
        def solve(i, j):

            if i > j:
                return 0
            if i==j:
                return 1

            if s[i] == s[j]:
                return 2 + solve(i + 1, j - 1)

            else:
                return max(solve(i, j - 1), solve(i + 1, j))

        return solve(0, len(s) - 1)
    
sol = Solution()
print(sol.longestPalindromeSubseq("bbbab"))
