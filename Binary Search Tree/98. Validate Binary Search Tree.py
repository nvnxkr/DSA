"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys strictly less than the node's key.
The right subtree of a node contains only nodes with keys strictly greater than the node's key.
Both the left and right subtrees must also be binary search trees.

 Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, node, limit):
        if not node:
            return True

        # Base condition
        if not limit[0] < node.val < limit[1]:
            return False

        left = self.solve(node.left, [limit[0], node.val])
        if left == False:
            return False
        right = self.solve(node.right, [node.val, limit[1]])

        return left and right

    def isValidBST(self, root: Optional[TreeNode]) -> bool:  # type: ignore
        return self.solve(root, [float("-inf"), float("inf")])
