# KAHN'S Algorithm

'''
Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, check whether it contains any cycle or not.
The graph is represented as a 2D vector edges[][], where each entry edges[i] = [u, v] denotes an edge from vertex u to v.

Examples:

Input: V = 4, edges[][] = [[0, 1], [1, 2], [2, 0], [2, 3]]



Output: true
Explanation: The diagram clearly shows a cycle 0 → 1 → 2 → 0
Input: V = 4, edges[][] = [[0, 1], [0, 2], [1, 2], [2, 3]]


Output: false
Explanation: no cycle in the graph
'''
from collections import deque


def isCyclic(self, V, edges):
    # code here
    adjList=[[] for _ in range(V)]
    
    indegree=[0]*V
    for u,v in edges:
        adjList[u].append(v)
        indegree[v]+=1
    
    q=deque()
    res=[]
    for i in range(len(indegree)):
        if indegree[i]==0:
            q.append(i)
    
    while q:
        e=q.popleft()
        res.append(e)
        
        for node in adjList[e]:
            indegree[node]-=1
            if indegree[node]==0:
                q.append(node)
    
    return len(res)!=V 
    