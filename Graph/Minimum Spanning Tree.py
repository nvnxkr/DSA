'''
Given a weighted, undirected, and connected graph with V vertices and E edges, your task is to find the sum of the weights of the edges in the Minimum Spanning Tree (MST) of the graph. The graph is provided as a list of edges, where each edge is represented as [u, v, w], indicating an edge between vertex u and vertex v with edge weight w.

Input: V = 3, E = 3, Edges = [[0, 1, 5], [1, 2, 3], [0, 2, 1]]
 
Output: 4
Explanation:

The Spanning Tree resulting in a weight
of 4 is shown above.
Input: V = 2, E = 1, Edges = [[0 1 5]]

 

Output: 5 
Explanation: Only one Spanning Tree is possible which has a weight of 5.
'''

import heapq

from networkx import edges


class Solution:
    def spanningTree(self, V, edges):
        # code here
        adj=[[] for _ in range(V)]
        
        for u,v,w in edges:
            adj[u].append([v,w])
            adj[v].append([u,w])
            
        total=0
        visited=[0 for _ in range(V)] # visited array
        
        pq=[[0,0,-1]]
        
        while pq:
            wt,node,parent=heapq.heappop(pq)
            
            if visited[node]==0:
                visited[node]=1
                total+=wt
                
                for adjNode,w in adj[node]:
                    if visited[adjNode]==0:
                        heapq.heappush(pq,[w,adjNode,node])
        
        return total


sol=Solution()
# print(sol.spanningTree(3, [[0, 1, 5], [1, 2, 3], [0, 2, 1]]))

Edges = [[0, 1, 5], [1, 2, 3], [0, 2, 1]]



print(Edges)