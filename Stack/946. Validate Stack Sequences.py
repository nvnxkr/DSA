# Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.

# Example 1:
# Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# Output: true

# Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
# Output: false



from typing import List


def validateStackSequences(pushed: List[int], popped: List[int]) -> bool:
    stack=[]
    n=len(pushed)
    j=0
    
    for i in pushed:
        stack.append(i)

        while stack and stack[-1]==popped[j]:
            stack.pop()
            j+=1

    return len(stack)==0


pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
print(validateStackSequences(pushed, popped))  # Output: true



    

