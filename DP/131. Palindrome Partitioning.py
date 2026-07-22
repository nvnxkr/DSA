'''
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 
'''

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        def ispalindrome(i, j):
            if i >= j:
                return True

            if s[i] == s[j]:
                return ispalindrome(i + 1, j - 1)

            return False

        def solve(start, res):
            if start == len(s):
                ans.append(res[:])
                return

            for i in range(start, n):
                if ispalindrome(start, i):
                    res.append(s[start : i + 1])
                    solve(i + 1, res)
                    res.pop()

        ans = []
        solve(0, [])
        return ans
