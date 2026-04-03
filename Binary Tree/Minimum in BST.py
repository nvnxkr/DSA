# Given the root of a Binary Search Tree. Your task is to find the minimum element in this given BST.

# Examples
# Input: root = [5, 4, 6, 3, N, N, 7, 1]

# Output: 1
# Explanation: The minimum element in the given BST is 1.
# Input: root = [10, 5, 20, 2]

# Output: 2
# Explanation: The minimum element in the given BST is 2.

"""
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
"""


def minValue(self, root):
    # code here
    temp=root
    mini=root.data
    
    while temp:
        
        mini=min(mini,temp.data)
        temp=temp.left
            
    return mini