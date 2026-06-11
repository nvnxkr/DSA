arr=[4, 6, 9, 12]

def soln(arr,ind):
    if ind>=len(arr):
        return True
    
    left=2*ind +1
    right=2*ind+2

    if left<len(arr) and arr[ind]>arr[left]:
        return False
    if right<len(arr) and arr[ind]>arr[right]:
        return False
    
    return soln(arr,left) and soln(arr,right)
    

print(soln(arr,0))