'''
Given an integer array arr[] and an integer k, reverse every consecutive group of k elements. If fewer than k elements remain at the end, reverse all of them.

Examples:

Input: arr[] = [1, 2, 3, 4, 5], k = 3
Output: [3, 2, 1, 5, 4]
Explanation: First group consists of elements 1, 2, 3. Second group consists of 4, 5.
Input: arr[] = [5, 6, 8, 9], k = 5
Output: [9, 8, 6, 5]
Explnation: Since k is greater than the number of remaining elements, the entire array is reversed.
'''

class Solution:

    def reverseInGroups(self, arr, k):
        """code here"""
        n=len(arr)
        ans=[]
        
        for i in range(0,n,k):
            ans+=arr[i:i+k][::-1]
            
        for i in range(n):
            arr[i]=ans[i]
        
        return arr
        

sol=Solution()
arr=[1, 2, 3, 4, 5]
k=3
print(sol.reverseInGroups(arr, k))  # Output: [3, 2, 1, 5, 4]

arr=[5, 6, 8, 9]
k=5
print(sol.reverseInGroups(arr, k))  # Output: [9, 8, 6, 5]