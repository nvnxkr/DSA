
from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    subset=[]
    result=[]
    def solve(ind,total,subset,nums,target,result):
        if total==target:
            result.append(subset.copy())
            return
        if total>target:
            return
        if ind>=len(nums):
            return

        Sum=total+nums[ind]
        subset.append(nums[ind])
        solve(ind,Sum,subset,nums,target,result)

        Sum=total
        subset.pop()
        solve(ind+1,Sum,subset,nums,target,result)
    

    solve(0,0,subset,candidates,target,result)

    return result

candidates = [2,3,6,7]
target = 7

print(combinationSum(candidates,target))