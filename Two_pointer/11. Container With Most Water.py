# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.


def maxArea(height) -> int:
    area=0
    i=0
    j=len(height)-1
    res=0

    while i < j :
        l=min(height[i],height[j])
        b=j-i
        area=l*b
        

        if height[i]<height[j]:
            i+=1
        else:
            j-=1

        res=max(area,res)

    return res

height = [1,8,6,2,5,4,8,3,7]

print(maxArea(height))