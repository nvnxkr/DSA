'''
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:

Input: text = "nlaebolko"
Output: 1

Example 2:

Input: text = "loonbalxballpoon"
Output: 2

Example 3:

Input: text = "leetcode"
Output: 0
'''

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        arr=[0]*26

        for ch in text:
            ind=ord(ch)-ord('a')
            arr[ind]+=1

        arr[ord('l')-ord('a')] //=2
        arr[ord('o')-ord('a')] //=2

        return min(
            arr[ord('b')-ord('a')],
            arr[ord('a')-ord('a')],
            arr[ord('l')-ord('a')],
            arr[ord('o')-ord('a')],
            arr[ord('n')-ord('a')]
        )

solution=Solution()
print(solution.maxNumberOfBalloons("loonbalxballpoon"))
