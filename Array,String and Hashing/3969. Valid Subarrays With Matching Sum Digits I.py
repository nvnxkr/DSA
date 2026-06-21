'''
You are given an integer array nums and an integer digit x.
A subarray nums[l..r] is considered valid if the sum of its elements satisfies both of the following conditions:

The first digit of the sum is equal to x.
The last digit of the sum is equal to x.
Return the number of valid subarrays.

Example 1:

Input: nums = [1,100,1], x = 1
Output: 4
Explanation:

The valid subarrays are:

nums[0..0]: sum = 1
nums[0..1]: sum = 1 + 100 = 101
nums[1..2]: sum = 100 + 1 = 101
nums[2..2]: sum = 1
Thus, the answer is 4.

Example 2:

Input: nums = [1], x = 2
Output: 0
Explanation:
The only subarray is nums[0..0] with a sum of 1, which does not satisfy the conditions.
Thus, the answer is 0.
'''

class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        n=len(nums)
        ans=0
        for i in range(n):
            total=0
            for j in range(i,n):
                total+=nums[j]

                firstdigit=int(str(total)[0])
                lastdigit=total%10

                if firstdigit==x and x==lastdigit:
                    ans+=1

        return ans
    
solution=Solution()
print(solution.countValidSubarrays([1,100,1], 1))
print(solution.countValidSubarrays([1], 2))