'''

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

'''

from typing import List


def subsets( nums: List[int]) -> List[List[int]]:
    n=len(nums)
    ans=[]
    
    
    def rec(ind,sub):
        if ind>=n:
            ans.append(sub.copy())
            return
        
        sub.append(nums[ind])
        rec(ind+1,sub)
        sub.pop()
        rec(ind+1,sub)

    rec(0,[])

    return ans


nums = [1,2,3]
print(subsets(nums))

