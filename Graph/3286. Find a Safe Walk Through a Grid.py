'''
You are given an m x n binary matrix grid and an integer health.

You start on the upper-left corner (0, 0) and would like to get to the lower-right corner (m - 1, n - 1).

You can move up, down, left, or right from one cell to another adjacent cell as long as your health remains positive.

Cells (i, j) with grid[i][j] = 1 are considered unsafe and reduce your health by 1.

Return true if you can reach the final cell with a health value of 1 or more, and false otherwise.

 

Example 1:

Input: grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], health = 1

Output: true

Explanation:

The final cell can be reached safely by walking along the gray cells below.


Example 2:

Input: grid = [[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]], health = 3

Output: false

Explanation:

A minimum of 4 health points is needed to reach the final cell safely.


Example 3:

Input: grid = [[1,1,1],[1,0,1],[1,1,1]], health = 5

Output: true

Explanation:

The final cell can be reached safely by walking along the gray cells below.



Any path that does not go through the cell (1, 1) is unsafe since your health will drop to 0 when reaching the final cell.

 
'''

from collections import deque
from typing import List


class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        q=deque()
        row=len(grid)
        col=len(grid[0])
        q.append((0,0))
        res=[[float('inf') for _ in range(col)] for _ in range(len(grid))]
        res[0][0]=grid[0][0]

        while q:
            i,j=q.popleft()

            for r,c in [(0,1),(1,0),(0,-1),(-1,0)]:
                nr=i+r
                nc=j+c

                if 0<=nr<row and 0<=nc<col:
                    if res[nr][nc]>res[i][j]+grid[nr][nc]:
                        res[nr][nc]=res[i][j]+grid[nr][nc]

                        if grid[nr][nc]==0:
                            q.appendleft((nr,nc))
                        else:
                            q.append((nr,nc))
            
        return res[-1][-1]<health
