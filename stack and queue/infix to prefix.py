class Solution:

    def precedence(self,ch):
        if ch=='+' or ch=="-":
            return 1
        elif ch=='*' or ch=='/':
            return 2
        elif ch=='^':
            return 3
        return -1
    
    def infixToPrefix(self,exp):
        stack=[]
        res=[]
        exp=exp[::-1]
        exp=exp.replace('(','temp')
        exp=exp.replace(')','(')
        exp=exp.replace('temp',')')

        
        for ch in exp:

            if ('a'<=ch<='z') or ('A'<=ch<='Z') or ('0'<=ch<='9'):
                res.append(ch)

            # if ch is (
            elif ch=='(':
                stack.append(ch)
            # if ch is )
            elif ch==')':
                while stack and stack[-1]!='(':
                    res.append(stack.pop())
                stack.pop()
            
            #if ch is operator
            else:
                while stack and self.precedence(stack[-1])>self.precedence(ch):
                    res.append(stack.pop())
                stack.append(ch)

        while stack:
            res.append(stack.pop())
        

        return ''.join(res[::-1])

s=Solution()
print(s.infixToPrefix("a+b*(c^d-e)^(f+g*h)-i"))
