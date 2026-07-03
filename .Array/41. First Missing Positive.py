'''
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
'''

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        contain1=False
        n=len(nums)

        for i in range(n):
            if nums[i]==1:
                contain1=True
            elif nums[i]<=0 or nums[i]>n:
                nums[i]=1
            
        if not contain1:
            return 1

        for i in range(n):
            num=abs(nums[i])
            if nums[num-1]>0:
                nums[num-1] *= -1 
        
        for i in range(n):
            if nums[i]>0:
                return i+1
        
        return n+1

solution=Solution()
print(solution.firstMissingPositive([1,2,0]))  # Output: 3
print(solution.firstMissingPositive([3,4,-1,1]))  # Output: 2
print(solution.firstMissingPositive([7,8,9,11,12]))  # Output: 1