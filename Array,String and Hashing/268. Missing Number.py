# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Example 1:
# Input: nums = [3,0,1]
# Output: 2
# Explanation:
# n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

from typing import List

def missingNumber(nums: List[int]) -> int:
    n=int(len(nums))
    sum=0

    for i in range(n):
        sum+=nums[i]

    total=(n*(n+1)/2)-sum

    return int(total)

# Example usage:
nums = [3,0,1]
print(missingNumber(nums))  # Output: 2
