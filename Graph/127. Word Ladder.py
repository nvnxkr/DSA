'''
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 
'''
# Algorithm

# Put all words from wordList into a set.
# If endWord is not in the set, return 0.
# Start BFS from beginWord.
# Pop one word from the queue.
# Change one character at a time (a to z) to generate new words.
# If the new word is in the set:
# Push it into the queue with steps + 1.
# Remove it from the set (mark as visited).
# If you reach endWord, return the number of steps.
# If the queue becomes empty, return 0.

from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word=set(wordList)
        if endWord not in word:
            return 0

        q=deque()
        q.append([beginWord,1])

        while q:
            curr,level=q.popleft()
            if curr==endWord:
                return level

            for i in range(len(curr)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    if ch==curr[i]:
                        continue
                    new_word=curr[:i]+ch+curr[i+1:]

                    if new_word in word:
                        q.append([new_word,level+1])
                        word.remove(new_word)

        return 0

sol=Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(sol.ladderLength(beginWord,endWord,wordList))
