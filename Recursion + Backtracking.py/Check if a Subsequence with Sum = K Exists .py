def solve(index,total,arr,target,subset,res):
    if total==target:
        res.append(subset.copy())
        return True
    elif total>target:
        return False
    if index==len(arr):
        return False
    
    subset.append(arr[index])
    
    pick=solve(index+1,total+arr[index],arr,target,subset,res)
    if pick:
        return True

    subset.pop()
    
    not_pick=solve(index+1,total,arr,target,subset,res)
    return not_pick


index=0
subset=[]
res=[]
arr=[1,4,5,6]
target=4
total=0
print(solve(index,total,arr,target,subset,res))
print(res)
