class Solution:

    def postfixToPrefix(self,exp):

        stack=[]
        opr='+-*%/^'

        for ch in exp:

            if ch in opr:
                first=stack.pop()
                second=stack.pop()
                res=f'{ch}{second}{first}'
                stack.append(res)
            else:
                stack.append(ch)

        return stack[-1]
s=Solution()
print(s.postfixToPrefix("abcd^e-fgh*+^*+i-"))