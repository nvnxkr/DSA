'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
'''

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2)<len(nums1):
            nums1,nums2=nums2,nums1
        m=len(nums1)
        n=len(nums2)
        total=m+n
        low=0
        high=m

        '''
              l1  r1
        [1,12,15, 26,38]
        [2,13,17, 30,45,60]
              l2  r2
        '''

        while low<=high: #Binary Search on small arr
            px=(low+high)//2  
            py=(total+1)//2-px 

            l1 = nums1[px - 1] if px > 0 else float('-inf')
            r1= nums1[px] if px < m else float('inf')

            l2 = nums2[py - 1] if py > 0 else float('-inf')
            r2= nums2[py] if py < n else float('inf')

            if l1<=r2 and l2<=r1:
                if total%2==0:
                    maxi=max(l1,l2)
                    mini=min(r1,r2)
                    return (mini+maxi)/2
                else:
                    return max(l1,l2)
            
            if l1>r2:
                high=px-1
            else:
                low=px+1

        return 0


solution=Solution()
print(solution.findMedianSortedArrays([1,3],[2]))
print(solution.findMedianSortedArrays([1,2],[3,4]))

            
 