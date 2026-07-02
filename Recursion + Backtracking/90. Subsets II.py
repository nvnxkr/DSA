'''
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
'''

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]

        def solve(ind,sub):
            if ind==len(nums):
                ans.append(sub[:])
                return 
            
            sub.append(nums[ind])
            solve(ind+1,sub)
            sub.pop()
            while ind+1<len(nums) and  nums[ind]==nums[ind+1]:
                ind+=1
            solve(ind+1,sub)
        solve(0,[])
        return ans
    
solution=Solution()
nums=[1,2,2]
print(solution.subsetsWithDup(nums))

            