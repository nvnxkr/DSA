# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
# You are giving candies to these children subjected to the following requirements:
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute the candies to the children.

# Example 1:
# Input: ratings = [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

# Example 2:
# Input: ratings = [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
# The third child gets 1 candy because it satisfies the above two conditions.



from typing import List


def candy(nums: List[int]) -> int:
    n=len(nums)
    candy=[1]*n
    ans=0
    

    for i in range(1,n):
        if nums[i]>nums[i-1]:
            candy[i]=candy[i-1]+1

    for i in range(n-2,-1,-1):
        if nums[i]>nums[i+1]:
            candy[i]=max(candy[i],candy[i+1]+1)


    return sum(candy)

ratings = [1,0,2]
print(candy(ratings))


        
        