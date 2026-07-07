'''
Given an undirected graph with V vertices numbered from 0 to V-1 and E edges, where edges[i] = [u, v] denotes an undirected edge between vertex u and vertex v, given two vertices src and dest, find the length of the shortest path from src to dest. If there is no path between src and dest, return -1.

Note: All edges have a unit weight of 1.

Examples :

Input: V = 9, edges[][] = [[0, 1], [0, 3], [1, 2], [3, 4], [4, 5], [2, 6], [5, 6], [6, 7], [6, 8], [7, 8]], src = 0, dest = 8
Output: 4
Explanation: One of the shortest paths from vertex 0 to vertex 8 is 0 -> 1 -> 2 -> 6 -> 8, which contains 4 edges.

Input: V = 4, edges[][]= [[0, 3], [1, 3]], src = 3, dest = 2
Output: -1
Explanation: There is no path between vertices 3 and 2.
'''

from collections import deque
class Solution:
    def shortestPath(self, V, edges, src, dest):
        # code here
        adjList=[[] for _ in range(V)]
        
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        dist=[-1]*V
        
        q=deque()
        q.append((src,0))
        
        while q:
            e,d=q.popleft()
            
            for node in adjList[e]:
                if dist[node]==-1:
                    q.append((node,d+1))
                    dist[node]=d+1
                    
                    
        
        return dist[dest]
    
sol=Solution()
V = 9
edges = [[0, 1], [0, 3], [1, 2], [3, 4], [4, 5], [2, 6], [5, 6], [6, 7], [6, 8], [7, 8]]
src = 0
dest = 8
print(sol.shortestPath(V, edges, src, dest))

