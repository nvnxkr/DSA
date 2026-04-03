from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)

one.left = two
two.left = three
two.right = four

one.right = five
five.left = six
five.right = seven


d = deque()
ans = []

root = one
d.append(root)

while d:
    n = d.popleft()
    ans.append(n.val)

    if n.left:
        d.append(n.left)
    if n.right:
        d.append(n.right)

print(ans)
