# Given the root of a binary tree, invert the tree, and return its root.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

def invertTree(root):
    

    def dfs(node):
        if node is None:
            return

        node.left,node.right=node.right,node.left

        if node.left:
            l=dfs(node.left)
        if node.right:
            r=dfs(node.right)

        

    dfs(root)

    return root




        
    