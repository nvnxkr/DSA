'''
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''

from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        freq = Counter(p)
        dic = {}
        x = len(p)
        n = len(s)
        if x > n:
            return []
        for i in range(x):
            ch = s[i]
            dic[ch] = dic.get(ch, 0) + 1
        ans = []
        if freq == dic:
            ans.append(0)
        j = x
        i = 0
        while j < n:
            dic[s[j]] = dic.get(s[j], 0) + 1
            dic[s[i]] -= 1
            if dic[s[i]] == 0:
                del dic[s[i]]
            if dic == freq:
                ans.append(i + 1)
            j += 1
            i += 1
        return ans
