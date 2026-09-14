'''
You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following mapping:

"1" -> 'A'

"2" -> 'B'

...

"25" -> 'Y'

"26" -> 'Z'

However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes ("2" and "5" vs "25").

For example, "11106" can be decoded into:

"AAJF" with the grouping (1, 1, 10, 6)
"KJF" with the grouping (11, 10, 6)
The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).
Note: there may be strings that are impossible to decode.

Given a string s containing only digits, return the number of ways to decode it. If the entire string cannot be decoded in any valid way, return 0.

The test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: s = "12"

Output: 2

Explanation:

"12" could be decoded as "AB" (1 2) or "L" (12).
'''

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [-1] * (n + 1)
        dp[n] = 1

        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
                continue
            one = dp[i + 1]
            two = 0
            if i + 1 < n and (s[i] == "1" or (s[i] == "2" and int(s[i + 1]) <= 6)):
                two = dp[i + 2]
            dp[i] = one + two

        return dp[0]

        """ dp=[-1]*(n+1)
        def solve(i):
            if i == n:
                dp[i]= 1
                return dp[i]
            one = two = 0
            if s[i] == "0":
                dp[i]=0
                return dp[i] 
            
            if dp[i]!=-1:
                return dp[i]

            one = solve(i + 1)

            if i + 1 < n and (s[i] == "1" or (s[i] == "2" and int(s[i + 1]) <= 6)):
                two = solve(i + 2)

            dp[i]=one + two
            return dp[i] 

        # return solve(0)"""
