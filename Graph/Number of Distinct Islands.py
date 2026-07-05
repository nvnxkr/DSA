'''
Given a grid grid[][] of size n × m, consisting of characters 'L' and 'W', where 'L' represents Land and 'W' represents Water, find the number of distinct islands in the grid. An island is a group of one or more land cells connected horizontally or vertically.

Two islands are considered distinct if their shapes are different.
Two islands have the same shape if one can be translated to match the other exactly. Rotation and reflection are not allowed.
Examples :

Input: grid[][] = [['L', 'W', 'W'], ['W', 'W', 'L'], ['L', 'W', 'W']]
Output: 1
Explanation: The grid contains three islands. All these islands have the same shape (a 1 × 1 block of land), so they are counted as a single distinct island.
 
Input: grid[][] = [['L', 'L', 'W', 'L', 'L'], ['L', 'W', 'W', 'W', 'W'], ['W', 'W', 'L', 'W', 'L'], ['L', 'W', 'W', 'L', 'L']]
Output: 4
Explanation: There are five islands in the grid. Two islands have the same shape (a 1 × 1 block of land), while the other three have different shapes. Therefore, the number of distinct island shapes is 4.
'''

class Solution:
    
    
    def dfs(self,i,j,br,bc,visited,grid,shape):
        row=len(grid)
        col=len(grid[0])
        if i<0 or i==row or j==col or j<0:
            return
        if visited[i][j]==1:
            return
        if grid[i][j]=='W':
            return
        visited[i][j]=1
        
        shape.append((i-br,j-bc))
        self.dfs(i+1,j,br,bc,visited,grid,shape)
        self.dfs(i-1,j,br,bc,visited,grid,shape)
        self.dfs(i,j+1,br,bc,visited,grid,shape)
        self.dfs(i,j-1,br,bc,visited,grid,shape)
        
    
    
    def countDistinctIslands(self, grid):
        # code here
        res=set()
        row=len(grid)
        col=len(grid[0])
        visited=[[0 for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if grid[i][j]=='L' and visited[i][j]==0:
                    br=i
                    bc=j
                    shape=[]
                    self.dfs(i,j,br,bc,visited,grid,shape)
                    res.add(tuple(shape))
        
        return len(res)
    
sol=Solution()
grid1=[['L', 'W', 'W'], ['W', 'W', 'L'], ['L', 'W', 'W']]
grid2=[['L', 'L', 'W', 'L', 'L'], ['L', 'W', 'W', 'W', 'W'], ['W', 'W', 'L', 'W', 'L'], ['L', 'W', 'W', 'L', 'L']]
print(sol.countDistinctIslands(grid1))  # Output: 1
print(sol.countDistinctIslands(grid2))  # Output: 4
