'''
Given a binary tree, determine if it is height-balanced.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def isBalanced(self, root) -> bool:

    def solve(node):
        if node is None:
            return 0

        left=solve(node.left)
        if left==-1:
            return -1
            
        right=solve(node.right)
        if right==-1:
            return -1
        

        if abs(left-right)>1:
            return -1

        return 1+max(left,right)

    return solve(root)!=-1

if __name__ == "__main__":
    # Example tree: [3,9,20,null,null,15,7]
    root = TreeNode(
        3,
        TreeNode(9),
        TreeNode(20, TreeNode(15), TreeNode(7)),
    )

    print("Is Balanced:", isBalanced(None, root))



    
    
    