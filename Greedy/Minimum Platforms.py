# Given arrival arr[] and departure dep[] times of trains on the same day, find the minimum number of platforms needed so that no train waits. A platform cannot serve two trains at the same time; if a train arrives before another departs, an extra platform is needed.
# Note: Time intervals are in the 24-hour format (HHMM) , where the first two characters represent hour (between 00 to 23 ) and the last two characters represent minutes (this will be <= 59 and >= 0). Leading zeros for hours less than 10 are optional (e.g., 0900 is the same as 900).

# Examples:
# Input: arr[] = [900, 940, 950, 1100, 1500, 1800], dep[] = [910, 1200, 1120, 1130, 1900, 2000]
# Output: 3
# Explanation: There are three trains during the time 9:40 to 12:00. So we need a minimum of 3 platforms.

from typing import List
def minPlatform(arr, dep):
    n=len(arr)
    arr.sort()
    dep.sort()
    count=1
    maxi=1
    i,j=1,0
    
    while i<n:
        if arr[i]<=dep[j]:
            count+=1
            i+=1
        else:
            count-=1
            j+=1
            
        maxi=max(count,maxi)
        
    return maxi
        
    

print(minPlatform([900, 940, 950, 1100, 1500, 1800],[910, 1200, 1120, 1130, 1900, 2000]))
print(minPlatform([200, 210, 300, 320, 350, 500],[230, 340, 320, 430, 400, 520]))
