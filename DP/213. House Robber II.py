# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

# Input: nums = [2,3,2]
# Output: 3


from typing import List


def rob(nums: List[int]) -> int:
    n=len(nums)
    
    def robbery(arr):
        n=len(arr)
        dp=[-1]*n
        dp[0]=arr[0]

        for i in range(1,n):
            if i>1:
                pick=arr[i]+dp[i-2]
            else:
                pick=arr[i]

            not_pick=dp[i-1]

            dp[i]=max(pick,not_pick)
        
        return dp[n-1]

    if n==1:
        return nums[0]
        
    ans1=robbery(nums[:n-1])
    ans2=robbery(nums[1:n])

    return max(ans1,ans2)

nums = [2,3,2]
print(rob(nums))  # Output: 3

nums = [1,2,3,1]
print(rob(nums))  # Output: 4