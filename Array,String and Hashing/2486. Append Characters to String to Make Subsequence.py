# You are given two strings s and t consisting of only lowercase English letters.
# Return the minimum number of characters that need to be appended to the end of s so that t becomes a subsequence of s.
# A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

# Example 1:
# Input: s = "coaching", t = "coding"
# Output: 4
# Explanation: Append the characters "ding" to the end of s so that s = "coachingding".
# Now, t is a subsequence of s ("coachingding").
# It can be shown that appending any 3 characters to the end of s will never make t a subsequence.

def appendCharacters(s: str, t: str) -> int:
    count=0
    n=len(s)
    m=len(t)
    i=j=0

    while i<n and j<m:
        if s[i]!=t[j]:
            i+=1
        else:
            i+=1
            j+=1

    return m-j

s = "coaching"
t = "coding"
print(appendCharacters(s, t))  # Output: 4
s = "abc"
t = "fce"
print(appendCharacters(s, t))  # Output: 3



