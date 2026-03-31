'''
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,2,3,4,null,null,null,5]
Output: [1,3,4,5]

Example 3:
Input: root = [1,null,3]
Output: [1,3]

Example 4:
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


def rightSideView(root):
    if not root:
        return []
    q=deque([root])
    ans=[]

    while q:
        n=len(q)

        ans.append(q[0].val)

        while n>0:
            node=q.popleft()

            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
            

            n-=1

    return ans

    