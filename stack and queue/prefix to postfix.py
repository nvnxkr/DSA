class Solution:

    def prefixToPostfix(self,exp):

        stack=[]
        opr='+-*%/^'

        for ch in reversed(exp):

            if ch in opr:
                first=stack.pop()
                second=stack.pop()
                res=f'{first}{second}{ch}'
                stack.append(res)
            else:
                stack.append(ch)

        return stack[-1]
s=Solution()
print(s.prefixToPostfix("-+a*b^-^cde+f*ghi"))