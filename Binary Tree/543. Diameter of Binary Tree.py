"""
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameterOfBinaryTree(root) -> int:
    diameter = 0

    def solve(node, count):
        nonlocal diameter

        if node is None:
            return 0

        left = solve(node.left, count + 1)
        right = solve(node.right, count + 1)

        diameter = max(diameter, left + right)

        return 1 + max(left, right)

    solve(root, 0)

    return diameter


'''

def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    count=0
    diameter=0

    def solve(node,count):
        nonlocal diameter

        if node is None:
            return 0

        left=solve(node.left,count+1)
        right=solve(node.right,count+1)

        diameter=max(diameter,left+right)

        return 1+max(left,right)

    solve(root,0)

    return diameter
'''


if __name__ == "__main__":
    # Example tree: [1,2,3,4,5]
    root = TreeNode(
        1,
        TreeNode(2, TreeNode(4), TreeNode(5)),
        TreeNode(3),
    )

    print("Diameter:", diameterOfBinaryTree(root))
