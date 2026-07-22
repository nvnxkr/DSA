'''
Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.
Example 2:

Input: nums = [1,2,4,8]
Output: [1,2,4,8]
'''

from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans=[]
        n=len(nums)
        def solve(ind,sub,ans):
            if ind==n:
                return sub[:]
            
            skip=solve(ind+1,sub,ans)

            take=[]
            if len(sub)==0 or nums[ind]%sub[-1]==0:
                sub.append(nums[ind])
                take=solve(ind+1,sub,ans)
                sub.pop()
            
            return skip if len(skip)>len(take) else take
        
        return solve(0,[],ans)


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        ans = []
        dp = [1 for _ in range(n)]
        prev_ind = [-1 for i in range(n)]
        maxLength = 1
        last_idx=0
        if len(nums) == 1:
            return nums

        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        prev_ind[i] = j

            if dp[i] > maxLength:
                maxLength = dp[i]
                last_idx = i

        while last_idx != -1:
            ans.append(nums[last_idx])
            last_idx = prev_ind[last_idx]

        return ans

sol = Solution()
nums = [1, 2, 3]
print(sol.largestDivisibleSubset(nums))