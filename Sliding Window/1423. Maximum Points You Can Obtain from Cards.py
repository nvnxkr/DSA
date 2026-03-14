# There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.
# In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.
# Your score is the sum of the points of the cards you have taken.
# Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

# Example 1:
# Input: cardPoints = [1,2,3,4,5,6,1], k = 3
# Output: 12
# Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.


from typing import List

def maxScore( nums: List[int], k: int) -> int:
    total=0
    n=len(nums)
    i,j=0,n-1

    while i<k:
        total+=nums[i]
        i+=1

    i-=1
    ans=total

    while i>=0:
        total=total-nums[i]+nums[j]
        ans=max(ans,total)
        i-=1
        j-=1

    return ans

print(maxScore([1,2,3,4,5,6,1],3))
