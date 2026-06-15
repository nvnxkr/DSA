'''
You are given a positive integer n.
Let digitSum be the sum of the digits of n, and let squareSum be the sum of the squares of the digits of n.
An integer is called good if squareSum - digitSum >= 50.
Return true if n is good. Otherwise, return false.

Example 1:

Input: n = 1000
Output: false

Explanation:

The digits of 1000 are 1, 0, 0, and 0.
The digitSum is 1 + 0 + 0 + 0 = 1.
The squareSum is 12 + 02 + 02 + 02 = 1.
The squareSum - digitSum is 1 - 1 = 0. As 0 is not greater than or equal to 50, the output is false.
Example 2:
'''

class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        ds=0
        ss=0
        while n>0:
            rem=n%10
            ds+=rem
            ss+=rem**2
            n//=10
        
        return ss-ds>=50
    
