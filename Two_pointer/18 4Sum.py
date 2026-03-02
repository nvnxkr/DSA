
# 18. 4Sum

# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

def fourSum(nums,target):
    nums.sort()
    
