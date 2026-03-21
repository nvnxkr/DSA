# Given an integer array height[] where height[i] represents the height of the i-th stair, a frog starts from the first stair and wants to reach the last stair. From any stair i, the frog has two options: it can either jump to the (i+1)th stair or the (i+2)th stair. The cost of a jump is the absolute difference in height between the two stairs. Determine the minimum total cost required for the frog to reach the last stair.

# Example:

# Input: heights[] = [20, 30, 40, 20]
# Output: 20
# Explanation:  Minimum cost is incurred when the frog jumps from stair 0 to 1 then 1 to 3:
# jump from stair 0 to 1: cost = |30 - 20| = 10
# jump from stair 1 to 3: cost = |20 - 30| = 10
# Total Cost = 10 + 10 = 20


# Recursion

''' 

def mini(ind,h):
    
    if ind==0:
        return 0
    
    jump1=mini(ind-1,h)+abs(h[ind]-h[ind-1])

    if ind>1:
        jump2=mini(ind-2,h) + abs(h[ind]-h[ind-2])
    else:
        jump2=float('inf')

    return min(jump1,jump2)

h=[20, 30, 40, 20]
n=len(h)-1
print(mini(n,h))

'''

# Memoization

def mini(ind,h):
    
    if ind==0:
        return 0
    
    if dp[ind]!=-1:
        return dp[ind]
    
    jump1=mini(ind-1,h)+abs(h[ind]-h[ind-1])

    if ind>1:
        jump2=mini(ind-2,h) + abs(h[ind]-h[ind-2])
    else:
        jump2=float('inf')

    dp[ind]=min(jump1,jump2)
    return dp[ind]

h=[20, 30, 40, 20]
n=len(h)
dp=[-1]*(n)
print(mini(n-1,h))


    