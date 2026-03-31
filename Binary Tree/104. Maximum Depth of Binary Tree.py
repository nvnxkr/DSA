"""
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3


"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# DFS approach

"""

def maxDepth(root) -> int:
    
    maxi = 0

    def traverse(node, count):
        nonlocal maxi

        if node is None:
            return

        maxi = max(maxi, count)

        traverse(node.left, count + 1)
        traverse(node.right, count + 1)

    traverse(root, 1)
    return maxi
"""

# BFS approach


from collections import deque



def maxDepth(root):
    queue = deque([root])
    count = 0
    if not root:
        return 0

    while queue:

        for _ in range(len(queue)):
            e = queue.popleft()

            if e.left:
                queue.append(e.left)
            if e.right:
                queue.append(e.right)

        count += 1

    return count


if __name__ == "__main__":
    # Example tree: [3,9,20,null,null,15,7]
    root = TreeNode(
        3,
        TreeNode(9),
        TreeNode(20, TreeNode(15), TreeNode(7)),
    )

    print("Max depth:", maxDepth(root))
