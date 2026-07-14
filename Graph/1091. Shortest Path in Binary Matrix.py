'''
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

 

Example 1:


Input: grid = [[0,1],[1,0]]
Output: 2
Example 2:


Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
'''

from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)
        q=deque()
        visited=[[0]*n for _ in range(n)]

        cnt=-1
        if grid[0][0]==0:
            q.append((0,0))
            cnt=1
            visited[0][0]=1
        
        dirs=[(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]

        while q:
            for _ in range(len(q)):
                i,j=q.popleft()
                if i==n-1 and j==n-1:
                    return cnt 
                for r,c in dirs:
                    nr=i+r
                    nc=j+c
                    if 0<=nr<n and 0<=nc<n:
                        if grid[nr][nc]==0 and visited[nr][nc]==0:
                            q.append((nr,nc))
                            visited[nr][nc]=1
            cnt+=1
        
        return -1

