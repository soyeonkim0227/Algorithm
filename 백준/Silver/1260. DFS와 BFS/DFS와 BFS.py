from collections import deque

N, M, V = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

bfs_vis = [0] * (N+1)
dfs_vis = [0] * (N+1)
queue = deque()

def bfs(first):
    queue.append(first)
    bfs_vis[first] = 1
    while len(queue) != 0:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, N+1):
            if not bfs_vis[i] and graph[v][i]:
                bfs_vis[i] = 1
                queue.append(i)

def dfs(v):
    print(v, end=' ')
    for i in range(1, N+1):
        if not dfs_vis[i] and graph[v][i]:
            dfs_vis[i] = 1
            dfs(i)

dfs_vis[V] = 1
dfs(V)

print()

bfs(V)