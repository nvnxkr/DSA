'''

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]


'''
from typing import List


def solveNQueens(n: int) -> List[List[str]]:
    ans=[]
    board=['.'*n for _ in range(n)]
    left=[0]*n
    lowerDiagonal=[0]*(2*n-1)
    upperDiagonal=[0]*(2*n-1)

    def solve(col,ans,board,left,lowerDiagonal,upperDiagonal,n):
        if col==n:
            ans.append(board.copy())
            return
        
        for row in range(n):
            if (
                left[row]==0
                and lowerDiagonal[col+row]==0
                and upperDiagonal[n-1 + col-row]==0
            ):

                board[row]=board[row][:col] + 'Q' + board[row][col+1:]

                left[row]=1
                lowerDiagonal[col+row]=1
                upperDiagonal[n-1 + col-row]=1

                solve(col+1,ans,board,left,lowerDiagonal,upperDiagonal,n)

                board[row]=board[row][:col] + '.' + board[row][col+1:]

                left[row]=0
                lowerDiagonal[col+row]=0
                upperDiagonal[n-1 + col-row]=0

    solve(0,ans,board,left,lowerDiagonal,upperDiagonal,n)

    return ans


n = 5
print(solveNQueens(n))

