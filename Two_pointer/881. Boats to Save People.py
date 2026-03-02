# You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

# Return the minimum number of boats to carry every given person.

# Input: people = [3,2,2,1], limit = 3
# Output: 3
# Explanation: 3 boats (1, 2), (2) and (3)
# Example 3:

# Input: people = [3,5,3,4], limit = 5
# Output: 4
# Explanation: 4 boats (3), (3), (4), (5)


from typing import List

def numRescueBoats(people: list[int], limit: int) -> int:
    i=0
    j=len(people)-1
    count=0
    people.sort()

    while i<=j:
        if people[i]+people[j]<=limit:
            
            i+=1
            j-=1
        else:
            j-=1
        
        count+=1

    return count

people = [3,2,2,1]
limit = 3   
print(numRescueBoats(people, limit))