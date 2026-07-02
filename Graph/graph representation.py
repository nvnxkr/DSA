n = 5  # no. of rows
m = 6  # no. of columns
edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 4], [3, 5], [4, 5]]  # edges of the graph

# Adjacency matrix

matrix = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for u, v in edges:
    matrix[u][v] = 1
    matrix[v][u] = 1

for row in matrix:
    print(row)


# Using list

lst = [[] for _ in range(n + 1)]

print(lst)
for u, v in edges:
    lst[u].append(v)
    lst[v].append(u)

print(lst)
