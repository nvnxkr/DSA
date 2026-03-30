'''

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

'''

from typing import List
def generateParenthesis(n: int) -> List[str]:
    bracket= [' ']* (2*n)
    result=[]
    
    def solve(ind,total,bracket,result):
        if ind>=len(bracket):
            if total==0:
                result.append(''.join(bracket))
            return
        
        if total> len(bracket)//2:
            return
        elif total<0:
            return

        bracket[ind]='('
        sum1=total+1
        solve(ind+1,sum1,bracket,result)

        bracket[ind]=')'
        sum1=total-1
        solve(ind+1,sum1,bracket,result)

    solve(0,0,bracket,result)
    return result

n = 3
print(generateParenthesis(n))

