def nextLargerElement( arr):
        # code here
    ans=[-1]*len(arr)
    stack=[]
    for i in range(len(arr)-1,-1,-1):
        
        while len(stack)!=0 and stack[-1]<=arr[i]:
            stack.pop()
            
        if len(stack)!=0:
            ans[i]=stack[-1]
        
        stack.append(arr[i])
        
    return ans

res=nextLargerElement([1, 3, 2, 4])
print(res)