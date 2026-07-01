class Solution:
    def quickSort(self, arr, low, high):
        # code here 
        if low>=high:
            return
        pi=self.partition(arr,low,high)
        self.quickSort(arr,low,pi-1)
        self.quickSort(arr,pi+1,high)

    def partition(self, arr, low, high):
        # code here
        pivot=arr[high]
        pi=low
        
        for i in range(low,high):
            if arr[i]<=pivot:
                arr[i],arr[pi]=arr[pi],arr[i]
                pi+=1
        
        arr[high],arr[pi]=arr[pi],arr[high]
        
        return pi

solution=Solution()
arr=[10,7,8,9,1,5]
solution.quickSort(arr,0,len(arr)-1)
print(arr)