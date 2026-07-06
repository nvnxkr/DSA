'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
'''

from typing import List


class Solution:
    def dfs(self,i,j,visited,grid):
        row=len(grid)
        col=len(grid[0])
        if i<0 or i==row or j<0 or j==col:
            return
        if visited[i][j]==1:
            return 
        if grid[i][j]=='0':
            return
        visited[i][j]=1
        self.dfs(i+1,j,visited,grid)
        self.dfs(i-1,j,visited,grid)
        self.dfs(i,j+1,visited,grid)
        self.dfs(i,j-1,visited,grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        row=len(grid)
        col=len(grid[0])

        
        visited=[[0 for _ in range(col)] for _ in range(row)]
        cnt=0

        for i in range(row):
            for j in range(col):
                if grid[i][j]=='1' and visited[i][j]==0:
                    cnt+=1
                    self.dfs(i,j,visited,grid)
                    

        return cnt


    # USING BFS
    '''
    def bfs(self,i,j,visited,grid):
        row=len(grid)
        col=len(grid[0])
        q=deque()
        q.append([i,j])
        visited[i][j]=1

        dirs=[[0,1],[1,0],[0,-1],[-1,0]]
        while q:
            
            x,y=q.popleft()

            for r,c in dirs:
                nr=x+r
                nc=y+c
                if 0<=nr<row and 0<=nc<col:
                    if grid[nr][nc]=='1' and visited[nr][nc]==0:
                        q.append([nr,nc])
                        visited[nr][nc]=1
    '''


sol=Solution()
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(sol.numIslands(grid))

grid = [
  ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
print(sol.numIslands(grid))