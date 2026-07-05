'''
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

 

Example 1:


Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.
Example 2:


Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.
 
'''

from collections import deque
from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        q=deque()

        for i in range(row):
            for j in range(col):
                if i==0 or j==0 or i==row-1 or j==col-1:
                    if grid[i][j]==1:
                        q.append([i,j])
                        grid[i][j]='#'
        
        dirs=[(1,0),(0,1),(-1,0),(0,-1)]
        while q:
            i,j=q.popleft()

            for r,c in dirs:
                nr=i+r
                nc=j+c
                if 0<=nr<row and 0<=nc<col:
                    if grid[nr][nc]==1:
                        grid[nr][nc]='#'
                        q.append([nr,nc])
        cnt=0
        
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    cnt+=1
        
        return cnt
        
sol=Solution()
grid=[[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
print(sol.numEnclaves(grid))

grid=[[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
print(sol.numEnclaves(grid))
