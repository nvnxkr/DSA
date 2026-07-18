'''
Given an undirected graph with V vertices numbered from 0 to V-1 and E edges, represented as a 2D array edges[][], where each entry edges[i] = [u, v] denotes an edge between vertices u and v. Count the number of connected components in the graph. Two vertices belong to the same connected component if there is a path between them.

Examples :

Input: V = 5, edges[][] = [[0, 1], [2, 1], [3, 4]]
Output: 2
Explanation:

Input: V = 7, edges[][] = [[0, 1], [6, 0], [2, 4], [2, 3], [3, 4]]
Output: 3

'''

class DisJointSet:
    def __init__(self,V):
        self.parent=[i for i in range(V+1)]
        self.rank=[0]*(V+1)
    
    def find(self,x):
        if x==self.parent[x]:
            return x
        
        self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,u,v):
        pu=self.find(u)
        pv=self.find(v)
        if pu==pv:
            return
        
        if self.rank[pu]<self.rank[pv]:
            self.parent[pu]=pv
        elif self.rank[pu]>self.rank[pv]:
            self.parent[pv]=pu
        else:
            self.parent[pu]=pv
            self.rank[pv]+=1

class Solution:
    def countConnected(self, V, edges):
        # code here 
        dsu=DisJointSet(V)
        for u,v in edges:
            dsu.union(u,v)
        
        seen=set()
        cnt=0

        for i in range(V):
            seen.add(dsu.find(i))
        
        return len(seen)

        
sol=Solution()
print(sol.countConnected(5, [[0, 1], [2, 1], [3, 4]]))