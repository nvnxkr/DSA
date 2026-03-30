from typing import List


def combinationSum3( k: int, n: int) -> List[List[int]]:
    arr=[1,2,3,4,5,6,7,8,9]

    subset=[]
    result=[]

    def solve(ind,subset,total):
        if len(subset)==k and total==n:
            result.append(subset[:])
            return
        if ind == len(arr) or total > n or len(subset) > k:
            return
    
        subset.append(arr[ind])
        solve(ind+1,subset,total+arr[ind])
        subset.pop()
        solve(ind+1,subset,total)

    solve(0,subset,0)

    return result

k=3
n=9
print(combinationSum3(k,n)) 