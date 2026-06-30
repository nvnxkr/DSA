'''
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

Example 1:
Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

'''

import random
class RandomizedSet:

    def __init__(self):
        self.sett=set()
        

    def insert(self, val: int) -> bool:
        if val not in self.sett:
            self.sett.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.sett:
            self.sett.remove(val)
            return True
        return False
        

    def getRandom(self) -> int:
        value=random.choice(list(self.sett))
        return value
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

randomSet = RandomizedSet()
print(randomSet.insert(1))
print(randomSet.remove(2))
print(randomSet.insert(2))
print(randomSet.getRandom())
print(randomSet.remove(1))
print(randomSet.insert(2))
print(randomSet.getRandom())
