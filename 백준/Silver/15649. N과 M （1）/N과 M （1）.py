def bt(v):
    if len(v) == M:
        print(' '.join(v))
        return
    for i in range(1, N+1):
        if vis[i] == 0:
            vis[i] = 1
            bt(v + str(i))
            vis[i] = 0

N, M = map(int, input().split())
vis = [0] * (N+1)

bt("")