'''
There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

 

Example 1:

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
Example 2:

Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true
 
'''

from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n=1000
        diff=[0]*n

        for num,s,e in trips:
            diff[s]+=num
            if e<1000:
                diff[e]-=num
        
        curr_total=0

        for cap in diff:
            curr_total+=cap
            if curr_total>capacity:
                return False
        
        return True

sol = Solution()
print(sol.carPooling([[2,1,5],[3,3,7]], 4))  # Output: False
print(sol.carPooling([[2,1,5],[3,3,7]], 5))  # Output: True