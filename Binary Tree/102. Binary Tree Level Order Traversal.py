'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3
Input: root = []
Output: []
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


def levelOrder(root):

    if root is None:
        return []

    queue=deque([root])

    ans=[[root.val]]
    

    while queue:
        res=[]
        
        for i in range(len(queue)):
            node=queue.popleft()
            if node.left:
                queue.append(node.left)
                res.append(node.left.val)
            
            if node.right:
                queue.append(node.right)
                res.append(node.right.val)
                
        if res !=[]:
            ans.append(res)

    return ans

    