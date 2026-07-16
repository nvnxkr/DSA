'''
You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.

 

Example 1:

Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
Example 2:

Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
Example 3:

Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.
'''

from typing import List


class Solution:
    def longestStrChain(self, nums: List[str]) -> int:
        nums=sorted(nums,key=len)

        n=len(nums)
        dp=[1]*n

        for i in range(1,n):
            for j in range(i):
                if len(nums[i])==len(nums[j])+1:
                    first=nums[i]
                    second=nums[j]
                    cnt=0
                    x=y=0
                    while x<len(first) and y<len(second):
                        if first[x]!=second[y]: 
                            cnt+=1
                            x+=1
                        else:
                            y+=1
                            x+=1

                    if cnt>=2:
                        continue
                    
                    dp[i]=max(dp[i],dp[j]+1)
        
        return max(dp)
                

