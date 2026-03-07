# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
# Return intervals after the insertion.

# Example 1:

# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

def insert(nums, new):
    flag=False
    for i in range(len(nums)):
        if new[0]<nums[i][0]:
            nums.insert(i,new)
            flag=True
            break
    if flag is False:
        nums.append(new)
        
    merge=[]

    for num in nums:
        if not merge or merge[-1][1]<num[0]:
            merge.append(num)
        else:
            merge[-1][1]=max(merge[-1][1],num[1])

    return merge


intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]

print(insert(intervals,newInterval))