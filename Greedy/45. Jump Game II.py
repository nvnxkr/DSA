# You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.
# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:0 <= j <= nums[i] and i + j < n
# Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

from typing import List
def jump( nums: List[int]) -> int:
    low=0
    n=len(nums)
    high=0
    jump=0

    while high<n-1:
        largest=0

        for i in range(low,high+1):
            largest=max(largest,i+nums[i])

        low=high+1
        high=largest
        jump+=1

    return jump

print(jump([2,3,1,1,4]))
print(jump([2,3,0,1,4]))


    
    
    

