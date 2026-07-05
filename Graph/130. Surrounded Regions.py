'''
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: A region is surrounded if none of the 'O' cells in that region are on the edge of the board. Such regions are completely enclosed by 'X' cells.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

 

Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation:


In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

Example 2:

Input: board = [["X"]]

Output: [["X"]]
'''

from collections import deque
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        q=deque()
        row=len(board)
        col=len(board[0])
        for i in range(row):
            for j in range(col):
                if i==0 or i==row-1 or j==0 or j==col-1:
                    if board[i][j]=='O':
                        q.append([i,j])
                        board[i][j]='#'
                
        
        
        dire=[(1,0),(0,1),(-1,0),(0,-1)]
        
        while q:

            for _ in range(len(q)):
                i,j=q.popleft()

                for r,c in dire:
                    newr=i+r
                    newc=j+c

                    if 0<=newr<row and 0<=newc<col:
                        if board[newr][newc]=='O':
                            board[newr][newc]='#'
                            q.append([newr,newc])

        for i in range(row):
            for j in range(col):
                if board[i][j]=='#':
                    board[i][j]='O'
                elif board[i][j]=='O':
                    board[i][j]='X'

        return board
        
        
sol=Solution()
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
print(sol.solve(board))

