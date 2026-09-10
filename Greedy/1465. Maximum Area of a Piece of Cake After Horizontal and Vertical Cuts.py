'''
You are given a rectangular cake of size h x w and two arrays of integers horizontalCuts and verticalCuts where:

horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, and
verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.
Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a large number, return this modulo 109 + 7.

 

Example 1:


Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
Output: 4 
Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green piece of cake has the maximum area.
Example 2:


Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
Output: 6
Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green and yellow pieces of cake have the maximum area.
Example 3:

Input: h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
Output: 9
'''

from typing import List


class Solution:
    def maxArea(self, h: int, w: int, hori: List[int], vert: List[int]) -> int:
        hori.sort()
        vert.sort()
        m = len(hori)
        n = len(vert)
        maxh = 0
        maxv = 0
        for i in range(1, m):
            maxh = max(maxh, hori[i] - hori[i - 1])
        for i in range(1, n):
            maxv = max(maxv, vert[i] - vert[i - 1])

        maxh = max(maxh, hori[0], h - hori[-1])
        maxv = max(maxv, vert[0], w - vert[-1])

        MOD = 10**9 + 7
        return (maxh * maxv) % MOD

sol = Solution()
print(sol.maxArea(5, 4, [1, 2, 4], [1, 3]))
print(sol.maxArea(5, 4, [3, 1], [1]))