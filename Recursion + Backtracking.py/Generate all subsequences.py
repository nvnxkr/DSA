def subsequence(index,valid,n,res,arr):
    if index==n:
        res.append(valid.copy())
        return
    
    valid.append(arr[index])
    subsequence(index+1,valid,n,res,arr)
    valid.pop()
    subsequence(index+1,valid,n,res,arr)

index=0
valid=[]
res=[]
arr=[1,2,3]
n=len(arr)
subsequence(index,valid,n,res,arr)
print(res)
    

