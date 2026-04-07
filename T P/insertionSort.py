def insertion(arr):
    n=len(arr)

    for i in range(n):
        j=i
        while j>0 and arr[j]<arr[j-1]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
            j-=1
    print(arr)

arr=[3,4,2,7,0,8,1]
insertion(arr)