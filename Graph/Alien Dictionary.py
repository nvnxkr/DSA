'''
A new alien language uses the English alphabet, but the order of letters is unknown. You are given a list of words[] from the alien language’s dictionary, where the words are claimed to be sorted lexicographically according to the language’s rules.
Your task is to determine the correct order of letters in this alien language based on the given words. If the order is valid, return a string containing the unique letters in lexicographically increasing order as per the new language's rules. If there are multiple valid orders, return any one of them.
However, if the given arrangement of words is inconsistent with any possible letter ordering, return an empty string ("").
A string a is lexicographically smaller than a string b if, at the first position where they differ, the character in a appears earlier in the alien language than the corresponding character in b. If all characters in the shorter word match the beginning of the longer word, the shorter word is considered smaller.

Note: Your implementation will be tested using a driver code. It will print true if your returned order correctly follows the alien language’s lexicographic rules; otherwise, it will print false.

Examples:

Input: words[] = ["baa", "abcd", "abca", "cab", "cad"]
Output: true
Explanation: A possible correct order of letters in the alien dictionary is "bdac".
The pair "baa" and "abcd" suggests 'b' appears before 'a' in the alien dictionary.
The pair "abcd" and "abca" suggests 'd' appears before 'a' in the alien dictionary.
The pair "abca" and "cab" suggests 'a' appears before 'c' in the alien dictionary.
The pair "cab" and "cad" suggests 'b' appears before 'd' in the alien dictionary.
So, 'b' → 'd' → 'a' → 'c' is a valid ordering.
Input: words[] = ["caa", "aaa", "aab"]
Output: true
Explanation: A possible correct order of letters in the alien dictionary is "cab".
The pair "caa" and "aaa" suggests 'c' appears before 'a'.
The pair "aaa" and "aab" suggests 'a' appear before 'b' in the alien dictionary. 
So, 'c' → 'a' → 'b' is a valid ordering.
Input: words[] = ["ab", "cd", "ef", "ad"]
Output: ""
Explanation: No valid ordering of letters is possible.
The pair "ab" and "ef" suggests "a" appears before "e".
The pair "ef" and "ad" suggests "e" appears before "a", which contradicts the ordering rules.
Constraints:
1 ≤ words.length ≤ 500
1 ≤ words[i].length ≤ 100
words[i] consists only of lowercase English letters.
'''


from collections import defaultdict, deque
class Solution:
    def findOrder(self, words):
        # code here
        adj = {c: [] for word in words for c in word}
        n=len(words)
        indegree=defaultdict(int)
        
        for i in range(n-1):
            w1=words[i]
            w2=words[i+1]
            x=0
            mini=min(len(w1),len(w2))
            while x<mini and w1[x]==w2[x]:
                x+=1
            
            if x==mini:
                if len(w1)>len(w2):
                    return ''
                
            else:
                if w2[x] not in adj[w1[x]]:
                    adj[w1[x]].append(w2[x])
                    indegree[w2[x]] += 1
        
        q=deque()
        res=[]
        for ch in adj:
            if indegree[ch]==0:
                q.append(ch)
        
        while q:
            e=q.popleft()
            res.append(e)
            
            for ch in adj[e]:
                indegree[ch]-=1
                if indegree[ch]==0:
                    q.append(ch)
        
        return '' if len(res)!=len(adj) else ''.join(res)
        
        
sol=Solution()
words = ["baa", "abcd", "abca", "cab", "cad"]
print(sol.findOrder(words))
