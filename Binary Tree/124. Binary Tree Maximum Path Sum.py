'''A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



def maxPathSum(self, root):
    
    
    self.maxi=float('-inf')

    def solve(node):

        if node is None:
            return 0

        left=solve(node.left)
        right=solve(node.right)

        niche_wala_ans = left + right + node.val  # left + right + node.val is the path which is passing through the node and going downwards in both direction

        koi_ek_accha = max(left,right) + node.val  # ya to left ya right se aayega path
        only_root_accha= node.val

        self.maxi = max(self.maxi , only_root_accha , koi_ek_accha , niche_wala_ans)

        # most imp

        return max(koi_ek_accha , only_root_accha) # niche_wala ans isliye nhi bheje  because we cannot go in both direction as it will be a cycle and we cannot have a cycle in a path

    solve(root)

    return self.maxi


