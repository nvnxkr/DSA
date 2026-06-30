# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

from typing import List
def sortColors(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    start=0
    mid=0
    end=len(nums)-1

    while mid<=end:
        if nums[mid]==0:
            nums[start],nums[mid]=nums[mid],nums[start]
            start+=1
            mid+=1

        elif nums[mid]==1:
            mid+=1

        else:
            nums[mid],nums[end]=nums[end],nums[mid]
            end-=1

nums = [2,0,2,1,1,0]
sortColors(nums)
print(nums)