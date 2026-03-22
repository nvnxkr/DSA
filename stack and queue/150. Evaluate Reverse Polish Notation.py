# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
# Evaluate the expression. Return an integer that represents the value of the expression.
# The valid operators are '+', '-', '*', and '/'.

# Example 1:
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:
# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6

from typing import List


def evalRPN(tokens: List[str]) -> int:
    stack=[]
    operator={'+','-','*','/'}

    for ch in tokens:

        if ch in operator:
            b=stack.pop()
            a=stack.pop()
            if ch=='+':
                stack.append(a+b)
            elif ch=='-':
                stack.append(a-b)
            elif ch=='*':
                stack.append(a*b)
            else:
                stack.append(int(a/b))

        else:
            stack.append(int(ch))

    return stack[-1]

tokens = ["2","1","+","3","*"]
print(evalRPN(tokens))
