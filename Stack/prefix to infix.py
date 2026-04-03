class Solution:
        
    def postfixToInfix(self,exp):

        stack=[]
        op='/*^+-'
        
        for ch in reversed(exp):
            if ch in op:
                top=stack.pop()
                sec=stack.pop()
                res=f'({top}{ch}{sec})'
                stack.append(res)
            
            else:
                stack.append(ch)

        return stack[-1]

s=Solution()
print(s.postfixToInfix("-+a*b^-^cde+f*ghi"))

