#Recursion
'''  
def fib(n):
    if n==0 :
        return 0
    elif n==1:
        return 1
    return fib(n-1)+fib(n-2)

print(fib(7))

'''

#Recursion + Memoization
'''

def fib(n,dp):
    if n==1:
        return 1
    if n==0:
        return 0
    if dp[n]!=-1:
        return dp[n]
    
    dp[n]=fib(n-1,dp) + fib(n-2,dp)
    return dp[n]
n=5
dp=[-1]*(n+1)
print(fib(n,dp))

'''

# Tabulation
'''
n=5
dp=[-1]*(n+1)

for i in range(n+1):
    if i<=1:
        dp[i]=i
    else:
        dp[i]=dp[i-1]+dp[i-2]
print(dp[5])
    
'''

#Tabulation with space optimization
'''
curr=2
prev1=1
prev2=0

n=7

for i in range(2,n+1):
    curr=prev1+prev2
    prev2=prev1
    prev1=curr
    

print(prev1)

'''

