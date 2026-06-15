'''
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
Return any possible rearrangement of s or return "" if not possible. 

Example 1:
Input: s = "aab"
Output: "aba"

Example 2:
Input: s = "aaab"
Output: ""
'''

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = {}
        for ch in s:
            count[ch]=count.get(ch,0)+1

        max_char = max(count, key=count.get)
        n = len(s)
        if count[max_char] > (n + 1) // 2:
            return ""

        result = [" "] * n
        i = 0

        while count[max_char]:
            result[i] = max_char
            i += 2
            count[max_char] -= 1

        for ch, freq in count.items():
            while freq:
                if i >= n:
                    i = 1
                result[i] = ch
                i += 2
                freq -= 1

        return "".join(result)
