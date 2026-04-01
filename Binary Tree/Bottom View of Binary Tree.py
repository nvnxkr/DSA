'''
You are given the root of a binary tree, and your task is to return its bottom view. The bottom view of a binary tree is the set of nodes visible when the tree is viewed from the bottom.
Note: If there are multiple bottom-most nodes for a horizontal distance from the root, then the latter one in the level order traversal is considered.

Examples :
Input: root = [1, 2, 3, 4, 5, N, 6]
Output: [4, 2, 5, 3, 6]
'''

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''


from collections import deque


def bottomView(root):
    dic={}
    line=0
    if not root:
        return []
    
    queue=deque([[root,line]])
    
    while queue:
        
        node,line = queue.popleft()
        dic[line]=node.data
        
        if node.left:
            queue.append([node.left,line-1])
            
        if node.right:
            queue.append([node.right,line+1])
            
    ans=[dic[i] for i in sorted(dic)]
    
    return ans
            
    
    
    