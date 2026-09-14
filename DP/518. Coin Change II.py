'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The final answer is guaranteed to fit into a signed 32-bit integer.

 

Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10]
Output: 1
'''

from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[-1] * 5000 for _ in range(n)]

        def solve(ind, total):
            if total == amount:
                return 1
            if total > amount:
                return 0
            if ind >= n:
                return 0
            if dp[ind][total] != -1:
                return dp[ind][total]

            take = solve(ind, total + coins[ind])
            skip = solve(ind + 1, total)

            dp[ind][total] = take + skip

            return dp[ind][total]

        return solve(0, 0)

sol = Solution()
print(sol.change(5, [1, 2, 5]))
print(sol.change(3, [2]))
print(sol.change(10, [10]))
