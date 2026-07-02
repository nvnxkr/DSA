n = 5  # no. of rows
m = 6  # no. of columns
edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 4], [3, 5], [4, 5]]  # edges of the graph

lst = [[] for _ in range(n + 1)]

for u, v in edges:
    lst[u].append(v)
    lst[v].append(u)

print(lst)

from collections import deque

def bfs(lst,ans,n):

    q=deque()
    visited=[0]*(n+1)

    q.append(0)
    visited[0]=1

    while q:
        e=q.popleft()
        ans.append(e)
        for node in lst[e]:
            if visited[node]==0:
                q.append(node)
                visited[node]=1
    return ans

print(bfs(lst,[],5))