# Given an array of integers arr[]  and a number k. Return the maximum sum of a subarray of size k.

# Note: A subarray is a contiguous part of any given array.

# Examples:

# Input: arr[] = [100, 200, 300, 400], k = 2
# Output: 700
# Explanation: arr2 + arr3 = 700, which is maximum.
# Input: arr[] = [1, 4, 2, 10, 23, 3, 1, 0, 20], k = 4
# Output: 39
# Explanation: arr1 + arr2 + arr3 + arr4 = 39, which is maximum.
# Input: arr[] = [100, 200, 300, 400], k = 1
# Output: 400
# Explanation: arr3 = 400, which is maximum.

class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        low=0
        high=k-1
        s=0
        res=0
        n=len(arr)
        
        for i in range(k):
            s+=arr[i]
        res=s
            
        while high<n-1:
            high+=1
            
            s= s-arr[low] + arr[high]
            low+=1
            res=max(res,s)
            
            
        return res