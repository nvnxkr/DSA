'''
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
'''

# using Recursion

class Solution:
    def countSubstrings(self, s: str) -> int:

        # def isPalindrome(st):
        #     n=len(st)
        #     i,j=0,n-1

        #     while i<j:
        #         if st[i]!=st[j]:
        #             return False
        #         i+=1
        #         j-=1

        #     return True

        n = len(s)
        dp = [[-1] * (n+1) for _ in range(n+1)]

        def isPalindrome(i, j):
            if i >= j:
                return 1

            if dp[i][j] != -1:
                return dp[i][j]

            if s[i] == s[j]:
                dp[i][j] = isPalindrome(i + 1, j - 1)
            else:
                dp[i][j] = 0

            return dp[i][j]

        cnt = 0

        for i in range(n):
            for j in range(i, n):
                if isPalindrome(i, j):
                    cnt += 1

        return cnt

# Top down approach

class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        dp=[[0]*(n+1) for _ in range(n+1)]
        cnt=0

        for l in range(1,n+1):
            for i in range(n-l+1):
                j=i+l-1
                if l==1:
                    dp[i][j]=1
                elif l==2:
                    dp[i][j]=1 if s[i]==s[j] else 0
                else:
                    if s[i]==s[j] and dp[i+1][j-1]==1:
                        dp[i][j]=1
                    
                if dp[i][j]==1: cnt+=1

        return cnt
                        

sol=Solution()
print(sol.countSubstrings("abc"))
