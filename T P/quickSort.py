def partition(arr,low,high):
    pivot=arr[low]
    i=low
    j=high

    while i<j:
        while arr[i]<=pivot and i<=high:
            i+=1
        while arr[j]>=pivot and j>=low:
            j-=1
        
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1

    arr[low],arr[high]=arr[high],arr[low]

    return j


