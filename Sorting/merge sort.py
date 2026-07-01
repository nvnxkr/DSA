
# code here
def merge(arr,l,mid,h):
    temp=[]
    i=l
    j=mid+1
    while i<=mid and j<=h:
        if arr[i]>arr[j]:
            temp.append(arr[j])
            j+=1
        else:
            temp.append(arr[i])
            i+=1
            
    while i<=mid:
        temp.append(arr[i])
        i+=1

    while j<=h:
        temp.append(arr[j])
        j+=1
    
    for idx in range(len(temp)):
        arr[l+idx]=temp[idx]
        

def mergeSort(arr,l,h):
    if l==h:
        return 
    mid=(l+h)//2
    # divide the array into two halves and sort them recursively
    mergeSort(arr,l,mid)  
    mergeSort(arr,mid+1,h)
    merge(arr,l,mid,h) # sorting is done by this
    
arr=[12,11,13,5,6,7]
mergeSort(arr,0,len(arr)-1)
print(arr)
