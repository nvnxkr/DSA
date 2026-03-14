# Ramu has N dishes of different types arranged in a row: A1,A2,…,AN where Ai denotes the type of the ith dish. He wants to choose as many dishes as possible from the given list but while sa sfying two conditions:
# •	He can choose only one type of dish.
# •	No two chosen dishes should be adjacent to each other.
# Ramu wants to know which type of dish he should choose from, so he can pick the maximum number of dishes.
# If multiple types give the same maximum count, return the smallest dish type.
# Example
# Input
# N = 9
# A = [1,2,2,1,2,1,1,1,1]

# Output
# 1
# Explanation:
# For type 1 , Ramu can choose at most four dishes. One of the ways to choose four dishes of type 1 is A1,A4, A7 and A9.
# For type 2 , Ramu can choose at most two dishes. One way is to choose A3 and A5.
# So in this case, Ramu should go for type 1 , in which he can pick more dishes.
# So answer = 1. 

n = 9
arr = [1,2,2,1,2,1,1,1,1]
j=2
i=0
maxi=float('-inf')
ans = float('inf')

while i<n:
    j=i
    count=0
    while j<n:
        
        if arr[j]==arr[i]:
            count+=1
            
            j+=2
        else:
            j+=1
    if count>maxi or (count==maxi and arr[i]<ans):
        maxi=max(maxi,count)
        ans=arr[i]
    i+=1

        
print(ans,maxi)