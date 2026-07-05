n = 5  # no. of rows
m = 6  # no. of columns
edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 4], [3, 5], [4, 5]]  # edges of the graph

lst = [[] for _ in range(n + 1)]

for u, v in edges:
    lst[u].append(v)
    lst[v].append(u)

print(lst)


visited=[0]*(n+1)
def dfs(lst,ans,n,start,visited):
    visited[start]=1
    ans.append(start)

    for node in lst[start]:
        if visited[node]==0:
            dfs(lst,ans,n,node,visited)
        
    return ans

print(dfs(lst,[],n,0,visited))

