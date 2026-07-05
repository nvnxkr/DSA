'''
Given an undirected graph with V vertices and E edges, represented as a 2D vector edges[][], where each entry edges[i] = [u, v] denotes an edge between vertices u and v, determine whether the graph contains a cycle or not.

Note: The graph can have multiple component.

Examples:

Input: V = 4, E = 4, edges[][] = [[0, 1], [0, 2], [1, 2], [2, 3]]
Output: true
Explanation: 
 
1 -> 2 -> 0 -> 1 is a cycle.
Input: V = 4, E = 3, edges[][] = [[0, 1], [1, 2], [2, 3]]
Output: false
Explanation: 
 
No cycle in the graph.
Constraints:
1 ≤ V, E ≤ 105
0 ≤ edges[i][0], edges[i][1] < V
'''

from collections import deque


class Solution:
    def isCycle(self, V, edges):
        # build adjacency list
        adj = [[] for _ in range(V)]
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        visited = [0] * V

        for i in range(V):
            if visited[i] == 1:
                continue

            q = deque()
            q.append([i, -1])
            visited[i] = 1

            while q:
                node, parent = q.popleft()
                for adjNode in adj[node]:
                    if visited[adjNode] == 0:
                        visited[adjNode] = 1
                        q.append([adjNode, node])
                    elif adjNode != parent:
                        return True

        return False


sol = Solution()
V = 4
E = 4
edges = [[0, 1], [0, 2], [1, 2], [2, 3]]

print(sol.isCycle(V, edges))
