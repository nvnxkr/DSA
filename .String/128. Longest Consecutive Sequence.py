# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

from typing import List
def longestConsecutive(nums: List[int]) -> int:
    sett=set(nums)
    res=0
    if len(nums)==0:
        return 0

    for num in sett:
        if num-1 not in sett:
            count=1
            i=1
            while num+i in sett:
                count+=1
                i+=1
            
            res=max(res,count)

    return res

nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))  # Output: 4
# Time complexity: O(n)
# Space complexity: O(n)
