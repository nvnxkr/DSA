"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

Example 1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:  # type: ignore
        n = len(nums)

        def helper(nums, st, end):
            if st > end:
                return None

            mid = (st + end) // 2

            root = TreeNode(nums[mid])  # type: ignore
            root.left = helper(nums, st, mid - 1)
            root.right = helper(nums, mid + 1, end)

            return root

        return helper(nums, 0, n - 1)
