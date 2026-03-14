# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

from typing import List

def rotate(nums,k):
    """
    Do not return anything, modify nums in-place instead.
    """
    k=k%len(nums)
    nums[:]=nums[-k:]+nums[:-k]

    return nums 

# Example usage:
nums = [1,2,3,4,5,6,7]
k = 3
print(rotate(nums, k))  # Output: [5,6,7,1,2,3,4]
