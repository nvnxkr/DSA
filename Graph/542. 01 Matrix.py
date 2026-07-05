'''
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two cells sharing a common edge is 1.

 

Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
'''

from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row=len(mat)
        col=len(mat[0])
        res=[[-1 for _ in range(col)] for _ in range(row)]
        q=deque()

        for i in range(row):
            for j in range(col):
                if mat[i][j]==0:
                    res[i][j]=0
                    q.append([i,j])
        
        dire=[(1,0),(0,1),(-1,0),(0,-1)]

        while q:
            i,j=q.popleft()

            for r,c in dire:
                nr=i+r
                nc=j+c

                if 0<=nr<row and 0<=nc<col and res[nr][nc]==-1:
                    res[nr][nc]=1+res[i][j]
                    q.append([nr,nc])
        
        return res


sol=Solution()
print(sol.updateMatrix([[0,1,1],[1,1,1],[1,1,1]]))  # Output: [[0,1,2],[1,2,3],[2,3,4]]
print(sol.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))  # Output: [[0,0,0],[0,1,0],[1,2,1]]


