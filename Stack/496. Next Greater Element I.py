# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.
# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

# Example 1:

# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]

from typing import List


def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    stack=[]
    n=len(nums2)
    dic={}
    ans=[]

    for i in range(n-1,-1,-1):
        while len(stack)!=0 and stack[-1]<=nums2[i]:
            stack.pop()
        
        if len(stack)!=0:
            dic[nums2[i]]=stack[-1]
        else:
            dic[nums2[i]]=-1

        stack.append(nums2[i])
    
    for num in nums1:
        # val=dic[nums]
        ans.append(dic[num])

    return ans

nums1 = [4,1,2]
nums2 = [1,3,4,2]
res=nextGreaterElement(0,nums1,nums2)
print(res)