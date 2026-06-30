# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
# Output: [1,2]

from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    dic={}
    ans=[]
    for num in nums:
        dic[num]=dic.get(num,0)+1

    while k!=0:
        result=max(dic , key=dic.get)
        ans.append(result)
        k-=1
        del dic[result]
    return ans

nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))