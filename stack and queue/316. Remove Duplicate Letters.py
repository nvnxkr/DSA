# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

# Example 1:
# Input: s = "bcabc"
# Output: "abc"

# Example 2:
# Input: s = "cbacdcbc"
# Output: "acdb"
 

def removeDuplicateLetters(s: str) -> str:
    stack=[]
    seen=set()

    for i in range(len(s)):
        ch=s[i]

        if ch in seen: continue

        while stack and ch<stack[-1] and stack[-1] in s[i+1:]:
            seen.remove(stack.pop())

        stack.append(ch)
        seen.add(ch)

    return ''.join(stack)


print(removeDuplicateLetters("bcabc"))
print(removeDuplicateLetters("cbacdcbc"))
