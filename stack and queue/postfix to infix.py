class Solution:
        
    def postfixToInfix(self,exp):

        stack=[]
        op='/*^+-'
        
        for ch in exp:
            if ch in op:
                top=stack.pop()
                sec=stack.pop()
                res=f'({sec}{ch}{top})'
                stack.append(res)
            
            else:
                stack.append(ch)

        return stack[-1]

s=Solution()
print(s.postfixToInfix("abcd^e-fgh*+^*+i-"))

