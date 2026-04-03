# Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.

# Example 1:
# Input: s = "bcabc"
# Output: "abc"

# Example 2:
# Input: s = "cbacdcbc"
# Output: "acdb"


def smallestSubsequence( s: str) -> str:
    stack=[]
    seen=set()
    i=0

    for i in range(len(s)):
        ch=s[i]

        if ch in seen:
            continue
        
        while stack and ch<stack[-1] and stack[-1] in s[i+1:]:
            seen.remove(stack.pop())

        stack.append(ch)
        seen.add(ch)

    return ''.join(stack)

print(smallestSubsequence("bcabc"))
print(smallestSubsequence("cbacdcbc"))
