'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
'''

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col=set()
        grid=set()
        
        # for row
        for i in range(9):
            row=set()
            for j in range(9):
                if board[i][j]=='.':
                    continue
                if board[i][j] in row:
                    return False
                row.add(board[i][j])

            
        # for column
        for j in range(9):
            col=set()
            for i in range(9):
                if board[i][j]=='.':
                    continue
                if board[i][j] in col:
                    return False
                col.add(board[i][j])

        
        # for grid
        def traversal(sr,er,sc,ec):
            grid=set()
            for i in range(sr,sr+3):
                for j in range(sc,sc+3):
                    if board[i][j]=='.':
                        continue
                    if board[i][j] in grid:
                        return False
                    grid.add(board[i][j])
                
            return True

        for sr in range(0,9,3):
            er=sr+2
            for sc in range(0,9,3):
                ec=sc+2
                if not traversal(sr,er,sc,ec):
                    return False

        return True

sol = Solution()
board1 = [["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]]

print(sol.isValidSudoku(board1))  # Output: True