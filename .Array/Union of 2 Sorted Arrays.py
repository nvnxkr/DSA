# Given two sorted arrays a[] and b[], where each array may contain duplicate elements , the task is to return the elements in the union of the two arrays in sorted order.
# Union of two arrays can be defined as the set containing distinct common elements that are present in either of the arrays.

# Examples:
# Input: a[] = [1, 2, 3, 4, 5], b[] = [1, 2, 3, 6, 7]
# Output: [1, 2, 3, 4, 5, 6, 7]
# Explanation: Distinct elements including both the arrays are: 1 2 3 4 5 6 7.

# Input: a[] = [2, 2, 3, 4, 5], b[] = [1, 1, 2, 3, 4]
# Output: [1, 2, 3, 4, 5]
# Explanation: Distinct elements including both the arrays are: 1 2 3 4 5.


def findUnion( a, b):
    # code here 
    n= len(a)
    m= len(b)
    result=[]
    i=0
    j=0
    
    while i<n and j<m:
        if a[i]<=b[j]:
            if len(result)==0 or result[-1]!=a[i]:
                result.append(a[i])
            i+=1
            
        else:
            if len(result)==0 or result[-1]!=b[j]:
                result.append(b[j])
            j+=1
            
    while i<n:
        if len(result)==0 or a[i]!=result[-1]:
                result.append(a[i])
        i+=1
    while j<m:
        if len(result)==0 or b[j]!=result[-1]:
                result.append(b[j])
        j+=1
                
                
    return result
        
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 6, 7]

print(findUnion(a, b))