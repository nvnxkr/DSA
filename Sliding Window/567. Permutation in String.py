'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
'''

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt = Counter(s1)
        n = len(s2)
        m = len(s1)
        freq = {}

        if n < m:
            return False
            
        for i in range(m):
            ch = s2[i]
            if ch not in freq:
                freq[ch] = 0
            freq[ch] += 1

        if cnt == freq:
            return True

        i = 0
        j = m
        while j < n:
            ch = s2[j]
            if ch not in freq:
                freq[ch] = 0
            freq[ch] += 1

            freq[s2[i]] -= 1
            if freq[s2[i]] == 0:
                del freq[s2[i]]

            if freq == cnt:
                return True
            j += 1
            i += 1

        return False

sol = Solution()
print(sol.checkInclusion("ab", "eidbaooo"))  # Output: True
print(sol.checkInclusion("ab", "eidboaoo"))  # Output: False