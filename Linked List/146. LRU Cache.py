'''
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
'''

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.limit = capacity

    def addNode(self, Node):
        nextNode = self.head.next
        self.head.next = Node
        Node.prev = self.head
        nextNode.prev = Node
        Node.next = nextNode

    def delNode(self, Node):
        prevNode = Node.prev
        nextNode = Node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode
        # del Node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        ansNode = self.map[key]
        ans = ansNode.val
        self.delNode(ansNode)
        # del self.map[key]
        self.addNode(ansNode)
        # self.map[key]=ansNode
        return ans

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            oldNode = self.map[key]
            self.delNode(oldNode)
            del self.map[key]

        if self.limit == len(self.map):
            lastNode = self.tail.prev
            del self.map[lastNode.key]
            self.delNode(lastNode)

        newNode = Node(key, value)
        self.addNode(newNode)
        self.map[key] = newNode


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)