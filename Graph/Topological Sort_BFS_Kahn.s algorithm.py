# KAHN'S Algorithm

'''
Given a Directed Acyclic Graph (DAG) of V (0 to V-1) vertices and E edges represented as a 2D list of edges[][], where each entry edges[i] = [u, v] denotes a directed edge u -> v. Return the topological sort for the given graph.

Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge u -> v, vertex u comes before v in the ordering.
Note: As there are multiple Topological orders possible, you may return any of them. If your returned Topological sort is correct then the output will be true else false.

Examples:

Input: V = 4, E = 3, edges[][] = [[3, 0], [1, 0], [2, 0]]

Output: true
Explanation: The output true denotes that the order is valid. Few valid Topological orders for the given graph are:
[3, 2, 1, 0]
[1, 2, 3, 0]
[2, 3, 1, 0]
'''

from collections import deque


def topoSort(V, edges):
    # Code here
    indegree=[0]*V
    adjList=[[] for _ in range(V)]
    
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
                
        
    return res


V=4
E=3
edges=[[3, 0], [1, 0], [2, 0]]

print(topoSort(V, edges))