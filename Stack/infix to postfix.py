class Solution:

    def precedence(self,ch):
        if ch=='+' or ch=="-":
            return 1
        elif ch=='*' or ch=='/':
            return 2
        elif ch=='^':
            return 3
        return -1
    
    def infixToPostfix(self,exp):
        stack=[]
        res=[]
        
        for ch in exp:

            if ('a'<=ch<='z') or ('A'<=ch<='Z') or ('0'<=ch<='9'): # ch.isalnum() -> same
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
                while stack and self.precedence(stack[-1])>=self.precedence(ch):
                    res.append(stack.pop())
                stack.append(ch)

        while stack:
            res.append(stack.pop())
        

        return ''.join(res)
    

s=Solution()
print(s.infixToPostfix("a+b*(c^d-e)^(f+g*h)-i"))

    