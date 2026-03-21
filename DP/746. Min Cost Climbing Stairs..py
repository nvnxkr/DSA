# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.

# Example 1:

# Input: cost = [10,15,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.

#Recursion
'''
def mini(ind,cost):
    if ind>=len(cost):
        return 0
    
    step1=mini(ind+1,cost) + cost[ind]
    step2=mini(ind+2,cost)+cost[ind]
    
    return min(step1,step2)

cost = [10,15,20]
print(min(mini(0,cost),mini(1,cost)))

'''

#Memoization
'''
def mini(ind,cost,dp):
    if ind>=len(cost):
        return 0

    if dp[ind]!=-1:
        return dp[ind]
    
    step1=mini(ind+1,cost,dp) + cost[ind]
    step2=mini(ind+2,cost,dp)+cost[ind]

    dp[ind]=min(step1,step2)
    return dp[ind]

cost = [10,15,20]
dp=[-1]*len(cost)
print(min(mini(0,cost,dp),mini(1,cost,dp)))
'''

#Tabulation
'''
cost = [10,15,20]
dp=[-1]*len(cost)
dp[0]=cost[0]
dp[1]=cost[1]
n=len(cost)

for ind in range(2,len(cost)):
    step1=dp[ind-1]+cost[ind]
    step2=dp[ind-2]+cost[ind]

    dp[ind]=min(step1,step2)

print(min(dp[n-1],dp[n-2]))

'''

# Tabulation with space optimization

'''
cost = [10,15,20]
        
prev2=cost[0]
prev=cost[1]
n=len(cost)

for ind in range(2,n):
    step1=prev+cost[ind]
    step2=prev2+cost[ind]

    curr=min(step1,step2)

    prev2=prev
    prev=curr

print(min(prev,prev2))
'''