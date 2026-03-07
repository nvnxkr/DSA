def merge(nums):
    n=len(nums)
    nums.sort()
    ans=[nums[0]]
    # maxi=0
    
    for i in range(1,n):
        if ans[-1][1]>=nums[i][0]:
            ans[-1][1]=max(ans[-1][1],nums[i][1])

        else:
            ans.append(nums[i])

    return ans

intervals = [[1,3],[2,6],[8,10],[15,18]]

print(merge(intervals))