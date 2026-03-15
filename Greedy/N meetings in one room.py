# You are given timings of n meetings in the form of (start[i], end[i]) where start[i] is the start time of meeting i and end[i] is the finish time of meeting i. Return the maximum number of meetings that can be accommodated in a single meeting room, when only one meeting can be held in the meeting room at a particular time. 
# Note: The start time of one chosen meeting can't be equal to the end time of the other chosen meeting.

# Examples :
# Input: start[] = [1, 3, 0, 5, 8, 5], end[] =  [2, 4, 6, 7, 9, 9]
# Output: 4
# Explanation: Maximum four meetings can be held with given start and end timings. The meetings are - (1, 2), (3, 4), (5,7) and (8,9)


def maximumMeetings(start,end):
    n=len(start)
    
    meeting=[(start[i],end[i]) for i in range(n)]
    
    meeting.sort(key =lambda x:x[1])
    
    last=meeting[0][1]
    count=1
    
    for i in range(1,n):
        if meeting[i][0]>last:
            count+=1
            last=meeting[i][1]
    
    return count
    
print(maximumMeetings([1, 3, 0, 5, 8, 5],[2, 4, 6, 7, 9, 9]))
print(maximumMeetings([75250, 50074, 43659, 8931, 11273, 27545, 50879, 77924],[112960, 114515, 81825, 93424, 54316, 35533, 73383, 160252]))
print(maximumMeetings([1, 2, 3],[2, 3, 4]))