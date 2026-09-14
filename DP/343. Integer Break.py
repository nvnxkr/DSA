'''
Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.

 

Example 1:

Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
'''

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [-1] * (n + 1)

        def solve(n):
            res = 0
            if n == 1:
                return 1

            if dp[n] != -1:
                return dp[n]

            for i in range(1, n):
                prod = i * max(n - i, solve(n - i))
                res = max(res, prod)
                """
                # Don't break n-i further
                a = i * (n - i)

                # Break n-i further
                b = i * solve(n - i)

                maxi = max(maxi, a, b)
                """
            dp[n] = res
            return dp[n]

        return solve(n)

sol = Solution()
print(sol.integerBreak(2))
print(sol.integerBreak(10))
