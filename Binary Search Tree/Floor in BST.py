"""
Given a root binary search tree and an integer x. your task is to find the greatest value node of the BST which is smaller than or equal to x.
Note: when x is smaller than the smallest node of BST then returns -1.

Examples:

Input:
                    2
                     \
                      81
                    /    \
                 42       87
                   \       \
                    66      90
                   /
                 45
x = 87
Output: 87
Explanation: 87 is present in tree so floor will be 87.
Input:
                          6
                           \
                            8
                          /   \
                        7       9
x = 11
Output: 9
Input:
                          6
                           \
                            8
                          /   \
                        7       9
x = 5
Output: -1
"""

"""
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
"""


def findFloor(root, x):
    # code here
    ans = -1
    while root:
        if root.data == x:
            return x

        elif root.data > x:
            root = root.left

        else:
            ans = root.data
            root = root.right

    return ans
