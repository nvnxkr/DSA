# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

from typing import List
def maxSubArray(nums: List[int]) -> int:
    maxi =float('-inf')
    total=0

    for i in range(len(nums)):
        total+=nums[i]
        maxi=max(maxi,total)

        if total<0:
            total=0

    return maxi # type: ignore
        
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))  # Output: 6
