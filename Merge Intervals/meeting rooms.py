# Given two arrays start[] and end[] such that start[i] is the starting time of ith meeting and end[i] is the ending time of ith meeting. Return the minimum number of rooms required to attend all meetings.

# Note: A person can also attend a meeting if it's starting time is same as the previous meeting's ending time.

# Input: start[] = [1, 10, 7], end[] = [4, 15, 10]
# Output: 1
# Explanation: Since all the meetings are held at different times, it is possible to attend all the meetings in a single room.

def minMeetingRooms(start, end):
    # code here
    start.sort()
    end.sort()
    
    i=0
    j=0
    count=0
    res=0
    
    while i<len(start) and j<len(end) :
        
        if start[i] < end[j]:
            count+=1
            i+=1
            res=max(res,count)
            
        else:
            count-=1
            j+=1
            
    return res

start = [2, 9, 6]
end= [4, 12, 10]

print(minMeetingRooms(start,end))