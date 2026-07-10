'''
Given two positive integers r and d of the same length, representing the current and desired lock configurations, respectively, where each digit corresponds to a circular ring numbered from 0 to 9, find the minimum number of rotations required to transform r into d.

In one operation, a ring can be rotated by one position either clockwise or anticlockwise.
The rings are circular, so 9 wraps to 0 and 0 wraps to 9.
Examples:

Input: r = 222, d = 333
Output: 3
Explaination: Each digit 2 can be changed to 3 in one rotation. Therefore, the minimum total rotations required are 1 + 1 + 1 = 3.
Input: r = 2345, d = 5432
Output: 8
Explaination: The minimum rotations required for the corresponding digit pairs (2, 5), (3, 4), (4, 3), and (5, 2) are 3, 1, 1, and 3, respectively. Therefore, the minimum total rotations required are 3 + 1 + 1 + 3 = 8.
'''

class Solution:

    def rotationCount(self, r, d):
        """ code here """
        cnt=0
        while r!=0 or d!=0:
            d1=r%10
            d2=d%10
            rotate=abs(d1-d2)
            
            cnt+=min(rotate,10-rotate)
            
            r//=10
            d//=10
        
        return cnt
            
sol=Solution()
print(sol.rotationCount(222, 333))

print(sol.rotationCount(2345, 5432))