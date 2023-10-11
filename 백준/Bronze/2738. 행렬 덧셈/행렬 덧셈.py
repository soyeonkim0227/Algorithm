N, M = map(int, input().split())

one = [list(map(int, input().split())) for _ in range(N)]
two = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        one[i][j] += two[i][j]
        print(one[i][j], end=' ')
    print()