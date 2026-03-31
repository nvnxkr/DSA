'''
You are given the root of a binary tree, and your task is to return its top view. The top view of a binary tree is the set of nodes visible when the tree is viewed from the top.

Note:
Return the nodes from the leftmost node to the rightmost node.
If multiple nodes overlap at the same horizontal position, only the topmost (closest to the root) node is included in the view. 

Examples:

Input: root = [1, 2, 3]
Output: [2, 1, 3]
Explanation: The Green colored nodes represents the top view in the below Binary tree.
 
Input: root = [10, 20, 30, 40, 60, 90, 100]
Output: [40, 20, 10, 30, 100]
Explanation: The Green colored nodes represents the top view in the below Binary tree.
'''

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque


def topView( root):
    # code here
    line=0
    dic={}
    ans=[]
    
    queue=deque([(root,line)])
    
    while queue:
        
        node,line = queue.popleft()
        
        if line not in dic:
            dic[line]=node.data
        
        if node.left:
            queue.append((node.left,line-1))
            
            
        if node.right:
            queue.append((node.right,line+1))
            
        
    for i in sorted(dic):
        ans.append(dic[i])
    
    # ans=sorted(dic,key=dic.get)
    
    return ans
        
        
        
        
        
        
        
        
        
        