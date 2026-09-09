'''
A string s is called happy if it satisfies the following conditions:

s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.
Example 2:

Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It is the only correct answer in this case.
'''

import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        arr = [[c, "c"], [b, "b"], [a, "a"]]
        ans = []

        while True:
            arr.sort(reverse=True)
            cnt1, ch1 = arr[0]
            if cnt1 == 0:
                break

            if len(ans) >= 2 and ans[-1] == ch1 and ans[-2] == ch1:
                cnt2, ch2 = arr[1]
                if cnt2 == 0:
                    break

                ans.append(ch2)
                arr[1][0] -= 1

            else:
                use = min(2, cnt1)
                ans.extend([ch1] * use)
                arr[0][0] -= use
        return "".join(ans)

sol = Solution()
print(sol.longestDiverseString(1, 1, 7))