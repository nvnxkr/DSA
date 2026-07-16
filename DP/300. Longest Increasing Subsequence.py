'''
Given an integer array nums, return the length of the longest strictly increasing subsequence.

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 
'''

# Recursive Approach:

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[[-1 for _ in range(n+1)] for _ in range(n+1)]
        def solve(ind,prev):
            if ind==len(nums):
                return 0
            
            if dp[ind][prev+1]!=-1:
                return dp[ind][prev+1]
            skip=solve(ind+1,prev)
            take=0
            if prev==-1 or nums[ind]>nums[prev]:
                take=solve(ind+1,ind)+1

            dp[ind][prev+1]=max(take,skip)
            return dp[ind][prev+1]

        return solve(0,-1)
    
# Bottom-Up Approach:


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[1 for _ in range(n+1)] 

        for i in range(n):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)


        return max(dp)
        