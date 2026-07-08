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

class Solution:
    def dfs(self,curr,visited,pathVisited,adjList):
        visited[curr]=1
        pathVisited[curr]=1
        
        for node in adjList[curr]:
            if visited[node]==0:
                if self.dfs(node,visited,pathVisited,adjList)==True:
                    return True
            if visited[node]==1 and pathVisited[node]==1:
                return True
            
        pathVisited[curr]=0
        return False
        
    
    
    def isCyclic(self, V, edges):
        # code here
        adjList=[[] for _ in range(V)]
        
        for u,v in edges:
            adjList[u].append(v)
        
        visited=[0]*V
        pathVisited=[0]*V
        for i in range(V):
            if visited[i]==0:
                if self.dfs(i,visited,pathVisited,adjList)==True:
                    return True
        
        return False

sol=Solution()
print(sol.isCyclic(4, [[0, 1], [1, 2], [2, 0], [2, 3]]))
