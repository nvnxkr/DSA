'''
There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.

 

Example 1:


Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
Example 2:


Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2
Example 3:

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: There are not enough cables.
 
'''

from typing import List


class Solution:
    def makeConnected(self, n: int, edges: List[List[int]]) -> int:

        parent = [i for i in range(n + 1)]
        rank = [0] * (n + 1)

        def find(x):
            if x ==parent[x]:
                return x

            parent[x] =find(parent[x])
            return parent[x]

        def union(u, v):
            nonlocal extra
            pu = find(u)
            pv = find(v)

            if pu == pv:
                extra += 1
                return

            if rank[pu] < rank[pv]:
                parent[pu] = pv
            elif rank[pu] > rank[pv]:
                parent[pv] = pu
            else:
                parent[pu] = pv
                rank[pv] += 1



        extra = components = 0
        for u, v in edges:
            union(u, v)
                

        for i in range(n):
            if find(i) == i:
                components += 1

        if extra >= components - 1:
            return components - 1

        return -1
