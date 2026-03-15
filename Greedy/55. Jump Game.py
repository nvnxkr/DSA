# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

from typing import List

def canJump(nums: List[int]) -> bool:
    step=nums[0]
    n=len(nums)
    i=1

    while i<n:
        if step==0:
            return False

        step-=1

        if nums[i]>step:
            step=nums[i]
            
        i+=1
            
    return True

print(canJump([2,3,1,1,4]))
print(canJump([3,2,1,0,4]))

