# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
# Example 1:

# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

from typing import List


def asteroidCollision(self, nums: List[int]) -> List[int]:
    stack=[]

    for num in nums:
        
        if num >0:
            stack.append(num)
        else:
            while stack and stack[-1]>0 and stack[-1]<abs(num):
                stack.pop()
            
            if stack and stack[-1]>0 and stack[-1]==abs(num):
                stack.pop()

            elif not stack or stack[-1]<0:
                stack.append(num)

    return stack

asteroids = [5,10,-5]
res=asteroidCollision(0,asteroids)
print(res)
