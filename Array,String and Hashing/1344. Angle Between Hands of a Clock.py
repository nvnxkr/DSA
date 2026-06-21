'''
Given two numbers, hour and minutes, return the smaller angle (in degrees) formed between the hour and the minute hand.

Answers within 10-5 of the actual value will be accepted as correct.

Example 1:
Input: hour = 12, minutes = 30
Output: 165

Example 2:
Input: hour = 3, minutes = 30
Output: 75

Example 3:
Input: hour = 3, minutes = 15
Output: 7.5

'''

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        mini=6 *minutes
        hr=30 * (hour%12) + 0.5 * minutes
        diff=abs(hr-mini)

        return min(diff,360-diff)
    
solution=Solution()
print(solution.angleClock(12,30))
print(solution.angleClock(3,30))
print(solution.angleClock(3,15))