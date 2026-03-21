# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

# Recursion
'''
def solve(ind,nums):
    if ind<0:
        return 0

    pick= solve(ind-2,nums) + nums[ind]
    notpick=solve(ind-1,nums)

    return max(pick,notpick)

nums = [2,7,9,3,1]
print(solve(len(nums)-1,nums))
'''

# Memoization

'''
def solve(ind,nums):
    if ind<0:
        return 0
    if dp[ind]!=-1:
        return dp[ind]

    pick= solve(ind-2,nums) + nums[ind]
    notpick=solve(ind-1,nums)
    dp[ind]= max(pick,notpick)
    return dp[ind]

nums = [2,7,9,3,1]
dp=[-1]*len(nums)
print(solve(len(nums)-1,nums))
'''


#Tabulation

'''
nums = [2,7,9,3,1]
dp=[-1]*len(nums)
dp[0]=nums[0]

for ind in range(1,len(nums)):
    pick=nums[ind]
    if ind>1:
        pick=pick+dp[ind-2]

    notpick=dp[ind-1]
    dp[ind]=max(pick,notpick)

print(dp[len(nums)-1])
'''

# Tabulation with space optimization


nums = [2,7,9,3,1]
n=len(nums)
prev=nums[0]
prev2=0

for ind in range(1,len(nums)):

    pick=nums[ind]+prev2
    not_pick=prev

    curr=max(pick,not_pick)

    prev2=prev
    prev=curr

print(prev)


